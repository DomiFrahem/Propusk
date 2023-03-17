from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot, QDate, QDateTime

from module.WorkWithDB import *
from module.MyMessageBox import show_dialog
from module.WorkWithCam import WorkWithCam, load_image
from module.TemplatePropusk import TemplatePropusk
from module.Printer import Printer
from module.lang.ru import *
from module.ImageTool import rotate_image


from .ui_py.ui_MainWindow import Ui_MainWindow
from .ListPersonal import ListPersonal
from .ListPlace import ListPlace
from .DialogSettingCam import SettingCam
from .DialogAbout import DialogAbout
from .DialogHistory import DialogHistory


from time import sleep
from datetime import datetime
from logger import logger
from pathlib import Path
import platform


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.date_from.setDateTime(QDateTime().currentDateTime())
        self.date_to.setDateTime(QDateTime().currentDateTime())

        self.stacked_widget_photo.currentChanged.connect(
            self.current_change_photo
        )

        self._init_menu_btn_action()
        self._init_push_btn_action()
        self._update_list_combobox()
        self._check_setting_cam()
        self._init_photo()

    def open_history(self) -> None:
        DialogHistory(self).exec_()

    def current_change_photo(self):
        if self.stacked_widget_photo.currentIndex() == os.environ.get('INDEX_CAMERA'):
            self.btn_start_cam_photo.setText(stop_cam)
        else:
            self.btn_start_cam_photo.setText(start_cam)

    def _init_menu_btn_action(self) -> None:
        self.action_open_history.triggered.connect(self.open_history)
        self.btn_show_personal_window.triggered.connect(
            self._show_personal_window
        )
        self.btn_show_place_window.triggered.connect(
            self._show_place_window
        )
        self.setting_cam.triggered.connect(
            self._show_setting_cam_window
        )
        self.update_list.triggered.connect(
            self._update_list_combobox
        )

        self.btn_show_about.triggered.connect(
            self._show_about_dialog
        )

    def _show_about_dialog(self):
        DialogAbout(self).exec_()

    def _check_setting_cam(self) -> None:
        if not self._get_selected_cam():
            logger.warning(warring_cams.get("title"))
            show_dialog(
                QMessageBox.Warning,
                warring_cams.get("title"),
                warring_cams.get("body")
            )

    def _init_push_btn_action(self) -> None:
        self.btn_start_cam_photo.clicked.connect(
            self._start_cam_photo
        )

        self.capturePhoto.clicked.connect(
            self._take_image_face
        )

        self.btn_save.clicked.connect(self._save)
        self.btn_clear.clicked.connect(self._clear)
        self.btn_print.clicked.connect(self._print)

    def _show_personal_window(self) -> None:
        ListPersonal(self).exec_()
        self._update_list_combobox()

    @Slot()
    def _show_place_window(self) -> None:
        ListPlace(self).exec_()
        self._update_list_combobox()

    @Slot()
    def _show_setting_cam_window(self) -> None:
        SettingCam(self).exec_()

    def _update_list_combobox(self) -> None:
        self._load_personal()
        self._load_place()

    def _load_personal(self) -> None:
        self.personal_combobox.clear()

        with connect() as conn:
            for personal in conn.execute(
                list_personal.select()
            ).all():
                fio = F"{personal.lastname} {personal.firstname} {personal.middlename}"
                self.personal_combobox.addItem(
                    fio,
                    userData={"id": personal.id}
                )

    def _load_place(self) -> None:
        self.place_combobox.clear()

        with connect() as conn:
            for place in conn.execute(
                list_place.select()
            ).all():
                self.place_combobox.addItem(
                    place.name_place,
                    userData={"id": place.id}
                )

    def _get_selected_cam(self) -> bool | str:
        with connect() as conn:
            cam = conn.execute(
                cam_setting.select()
            ).fetchone()

            try:
                return cam.selected_cam
            except:
                return False

    def _init_photo(self) -> None:
        load_image(self.imagePhoto, os.environ.get('NO_MEDIA_IMAGE'))

    @Slot()
    def _start_cam_photo(self) -> None:
        if self._get_selected_cam():
            if self.stacked_widget_photo.currentIndex() == int(os.environ.get('INDEX_PHOTO')):
                self.stacked_widget_photo.setCurrentIndex(
                    int(os.environ.get('INDEX_CAMERA')))
                self._create_wwc()

                self.face_wwc.start_cam()
            else:
                self.face_wwc.stop_cam()
                self.stacked_widget_photo.setCurrentIndex(
                    int(os.environ.get('INDEX_PHOTO')))

    def _create_wwc(self) -> None:
        if not hasattr(self, "face_wwc"):
            self.face_wwc = WorkWithCam(
                q_Video_Widget=self.face_video_widget,
                name_cam=self._get_selected_cam())

    @Slot()
    def _take_image_face(self) -> None:
        if hasattr(self, "face_wwc"):
            self.face_file_name = self.face_wwc.cupture_image(self.imagePhoto)

            sleep(1)
            self.stacked_widget_photo.setCurrentIndex(
                int(os.environ.get('INDEX_PHOTO')))
            self.face_wwc.stop_cam()

    @Slot()
    def _print(self) -> None:
        if not hasattr(self, "data_propusk"):
            self._save()

        propusk_data = self.data_propusk.copy()
        propusk_data["personal"] = self.personal_combobox.currentText()
        propusk_data["place"] = self.place_combobox.currentText()
        propusk_data["date_from"] = self.date_from.dateTime().toString(
            'dd.MM.yyyy hh:mm')
        propusk_data["date_to"] = self.date_to.dateTime().toString(
            'dd.MM.yyyy hh:mm')

        rotate_img = rotate_image(self.face_file_name, -90)
        
        if platform.system() in 'Linux':
            rotate_img = F"file://{rotate_img}"

        propusk_data["face_photo"] = rotate_img

        render_text = TemplatePropusk(
            propusk_data,
            os.path.join(os.environ.get('ABSOLUTE_PATH'), 'docs')
        )

        Printer(str(render_text)).print()

    @Slot()
    def _clear(self) -> None:
        if hasattr(self, "data_propusk"):
            del self.data_propusk

        self._set_default_data()

    @Slot()
    def _save(self) -> None:
        date_from = self.date_from.dateTime().toMSecsSinceEpoch() / 1000
        date_to = self.date_to.dateTime().toMSecsSinceEpoch() / 1000

        self.data_propusk = {
            "id_propusk": int(self.number_propusk.text()),
            "date_from": datetime.fromtimestamp(date_from),
            "date_to": datetime.fromtimestamp(date_to),
            "personal": self.personal_combobox.currentData()['id'],
            "place": self.place_combobox.currentData()['id'],
            "receiving_man": self.receiving_man.toPlainText(),
            "purpose_visite": self.purpose_visite.toPlainText(),
            "face_photo": F"{Path(self.face_file_name).name}",
            "pasport_photo": F"{Path(self.face_file_name).name}"
        }

        with connect() as conn:
            conn.execute(
                list_propusk.insert().values(**self.data_propusk)
            )

    def _set_default_data(self) -> None:
        self.number_propusk.clear()
        self.date_from.setDate(QDate().currentDate())
        self.date_to.setDate(QDate().currentDate())
        self._init_photo()
        self.receiving_man.clear()
        self.purpose_visite.clear()
        self.stacked_widget_photo.setCurrentIndex(
            int(os.environ.get('INDEX_PHOTO')))
        if hasattr(self, "face_wwc"):
            delattr(self, "face_wwc")
