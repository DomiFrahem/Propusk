from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QDate, QDateTime
from sqlalchemy.exc import OperationalError

from module.WorkWithDB import *
from module.MyMessageBox import show_dialog
from module.TemplatePropusk import TemplatePropusk
from module.Printer import Print
from module.lang.ru import *
from module.cam import IPCam, USBCam, load_image
from module import create_filename
from module.QRCode import make as make_qr

from widgets import PStackedWidget, create_widget_stacked

from .ui_py.ui_MainWindow import Ui_MainWindow
from .ListPersonal import ListPersonal
from .ListPlace import ListPlace
from .DialogSettingCam import SettingCam
from .DialogAbout import DialogAbout
from .DialogHistory import DialogHistory

from datetime import datetime
from logger import logger
from pathlib import Path
import sys

vecrot_cam_from_db = [str, str, str]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.__wwc = None
        self.data_propusk = None
        self.stacked_face = None

        self.date_from.setDateTime(QDateTime().currentDateTime())
        self.date_to.setDateTime(QDateTime().currentDateTime())

        self.__init_menu_action()
        self.__init_btn_action()
        self.__update_list_combobox()
        self.__check_setting_cam()
        self.__create_widget_face_cam()

        self.tabWidget.currentChanged.connect(
            self.change_tab
        )

    def __init_menu_action(self) -> None:
        self.action_open_history.triggered.connect(self.open_history)
        self.btn_show_personal_window.triggered.connect(
            self.__show_personal_window
        )
        self.btn_show_place_window.triggered.connect(
            self.__show_place_window
        )
        self.setting_cam.triggered.connect(
            self.__show_setting_cam_window
        )
        self.update_list.triggered.connect(
            self.__update_list_combobox
        )

        self.btn_show_about.triggered.connect(
            self.__show_about_dialog
        )

    def __init_btn_action(self) -> None:
        self.btn_start_cam.clicked.connect(
            self.__press_btn_start_cam
        )

        self.capturePhoto.clicked.connect(
            self.__take_image
        )

        self.btn_save.clicked.connect(self.__save)
        self.btn_clear.clicked.connect(self.__clear)
        self.btn_print.clicked.connect(self.__print)

    def __show_about_dialog(self):
        DialogAbout(self).exec_()

    def __show_personal_window(self) -> None:
        ListPersonal(self).exec_()
        self.__update_list_combobox()

    def __show_place_window(self) -> None:
        ListPlace(self).exec_()
        self.__update_list_combobox()

    def __show_setting_cam_window(self) -> None:
        self.__stop_cam()
        SettingCam(self).exec_()
        self.__check_setting_cam()
        self.__create_widget_face_cam()

    def open_history(self) -> None:
        DialogHistory(self).exec_()

    def change_tab(self) -> None:
        self.__stop_cam()
        self.__check_setting_cam()
        if self.tabWidget.currentIndex() == 1:
            self.__mode = 'video'

    def __check_setting_cam(self) -> None:
        try:
            self.__mode, self.__cam_face, self.__cam_document = self.__get_selected_cam()
        except ValueError:
            logger.warning(warring_cams.get("title"))
            if show_dialog(
                QMessageBox.Warning,
                warring_cams.get("title"),
                warring_cams.get("body")
            ):
                self.__show_setting_cam_window()
                self.__check_setting_cam()
            else:
                self.close()
        except TypeError:
            logger.warning(warring_cams.get("title"))

    def __update_list_combobox(self) -> None:
        self.__load_personal()
        self.__load_place()

    def __load_personal(self) -> None:
        self.personal_combobox.clear()

        with connect() as conn:
            for personal in conn.execute(
                list_personal.select()
            ).all():
                fio = F"{personal.lastname} {personal.firstname} {personal.middlename}"
                self.personal_combobox.addItem(
                    fio,
                    userData=personal.id
                )

    def __load_place(self) -> None:
        self.place_combobox.clear()

        with connect() as conn:
            for place in conn.execute(
                list_place.select()
            ).all():
                self.place_combobox.addItem(
                    place.name_place,
                    userData=place.id
                )

    def __get_selected_cam(self) -> vecrot_cam_from_db:
        '''
        return: 
            str -> video, snapshot
            str -> ссылка для подключения к ip камеры или названия камеры (для лица)
            str -> названия камеры (для документа)
        '''
        with connect() as conn:
            cam = conn.execute(
                cam_setting.select()
            ).all()

            try:
                return cam[0].mode, cam[0].selected_cam, cam[1].selected_cam
            except:
                logger.error('Нет записи о камерах')
                if show_dialog(
                    QMessageBox.Icon.Critical,
                    'Камера',
                    'Отсутствуют записи о камерах'
                ):
                    self.__show_setting_cam_window()
                    self.__check_setting_cam()
                else:
                    sys.exit(0)

    def __press_btn_start_cam(self):
        match self.tabWidget.currentIndex():
            case 0: self.__start_cam(self.stacked_face, self.__cam_face)
            case 1: self.__start_cam(self.stacked_document, self.__cam_document)

    def __start_cam(self, widget: PStackedWidget, cam: str) -> None:
        if self.__wwc is None:
            widget.to_video()
            self.__create_wwc(widget, cam)
            self.btn_start_cam.setText(stop_cam)

        else:
            self.__stop_cam()
            widget.to_image()
            self.btn_start_cam.setText(start_cam)

    def __create_wwc(self, widget: PStackedWidget, cam: str) -> None:
        if self.__mode in 'snapshot':
            self.__wwc = IPCam()
            self.__wwc.qLabel = widget.video
            self.__wwc.lnk_connect = cam
            self.__wwc.start()
        else:
            self.__wwc = USBCam(widget.video, cam)
            self.__wwc.start_cam()

    def __take_image(self) -> None:
        if self.tabWidget.currentIndex() == 1:
            self.__file_name_document = self.__wwc.cupture_image(
                self.stacked_document.image)
            self.stacked_document.to_image()
        else:
            self.__file_name_face = self.__wwc.cupture_image(
                self.stacked_face.image)
            self.stacked_face.to_image()

        self.btn_start_cam.setText(start_cam)

        # self.__stop_cam()

    def __print(self) -> None:
        if self.data_propusk is None:
            self.__save()

        propusk_data = self.data_propusk.copy()


        propusk_data.update({
            "personal": self.personal_combobox.currentText(),
            "place": self.place_combobox.currentText(),
            "date_from": self.date_from.dateTime().toString('dd.MM.yyyy hh:mm'),
            "date_to": self.date_to.dateTime().toString('dd.MM.yyyy hh:mm'),
            "face": self.__file_name_face,
            "document": self.__file_name_document,
            "qrcode": make_qr(propusk_data.get("id_propusk"), create_filename('qr')),
            "count_repeat": 2
        })

        render_text = TemplatePropusk(
            propusk_data,
            os.path.join(os.environ.get('ABSOLUTE_PATH'), 'docs')
        )

        Print(str(render_text))

    def __clear(self) -> None:
        if self.data_propusk is not None:
            self.data_propusk = None

        self.__set_default_data()

    def __save(self) -> None:
        date_from = self.date_from.dateTime().toMSecsSinceEpoch() / 1000
        date_to = self.date_to.dateTime().toMSecsSinceEpoch() / 1000

        self.data_propusk = {
            "id_propusk": int(self.number_propusk.text()),
            "date_from": datetime.fromtimestamp(date_from),
            "date_to": datetime.fromtimestamp(date_to),
            "personal": self.personal_combobox.currentData(),
            "place": self.place_combobox.currentData(),
            "receiving_man": self.receiving_man.toPlainText(),
            "purpose_visite": self.purpose_visite.toPlainText(),
            "face": F"{Path(self.__file_name_face).name}",
            "document": F"{Path(self.__file_name_document).name}"
        }

        with connect() as conn:
            try:
                conn.execute(
                    list_propusk.insert().values(**self.data_propusk)
                )

                show_dialog(QMessageBox.Icon.Information, '', 'Сохранено')
            except OperationalError as er:
                logger.error(er)
                show_dialog(QMessageBox.Icon.Critical, 'Ошибка',
                            'Произошла ошибка при сохранении! \n Обратитесь к администратору')

    def __set_default_data(self) -> None:
        self.number_propusk.clear()
        self.date_from.setDate(QDate().currentDate())
        self.date_to.setDate(QDate().currentDate())

        if self.__wwc is not None:
            self.__stop_cam()

        self.stacked_document.to_image()
        self.stacked_face.to_image()
        load_image(self.stacked_document, os.environ.get('NO_MEDIA_IMAGE'))
        load_image(self.stacked_face, os.environ.get('NO_MEDIA_IMAGE'))

        self.receiving_man.clear()
        self.purpose_visite.clear()

    def __stop_cam(self):
        if self.__wwc is not None:
            self.__wwc.stop_cam()
            self.__wwc = None

        self.btn_start_cam.setText(start_cam)

    def __create_widget_face_cam(self) -> None:
        self.gridLayout.removeWidget(self.stacked_face)

        self.stacked_face = create_widget_stacked(
            name_object=u'stacked_face',
            obj=self.tab,
            layout=self.gridLayout,
            mode=self.__mode)

        self.stacked_face.currentChanged.connect(
            self.__change_text_btn
        )

    def __change_text_btn(self) -> None:
        if self.stacked_face.currentIndex() == 0:
            self.btn_start_cam.setText(stop_cam)
        else:
            self.btn_start_cam.setText(start_cam)
