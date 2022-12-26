from PySide6.QtWidgets import (
    QMainWindow, QMessageBox)
from PySide6.QtCore import Slot, QDate
from PySide6.QtGui import QImage, QRegularExpressionValidator

from module.WorkWithDB import *
from module.MessageBox import showDialog
from module.WorkWithCam import WorkWithCam, load_image
from module.TemplatePropusk import TemplatePropusk
from module.Printer import Printer

from .ui_py.ui_MainWindow import Ui_MainWindow
from .ListPersonal import ListPersonal
from .ListPlace import ListPlace
from .SettingCam import SettingCam

from time import sleep
from datetime import datetime


NO_MEDIA_IMAGE = "image/no_media_main.jpg"
INDEX_PHOTO = 0
INDEX_CAMERA = 1
ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__package__))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        print("Hi main window")
        self.number_propusk.setValidator(QRegularExpressionValidator(
            r"\d+", self
        ))

        # self._set_default_data()

        self._init_menu_btn_action()
        self._init_push_btn_action()
        self._update_list_combobox()
        self._check_setting_cam()
        self._init_photo()

    def _init_menu_btn_action(self) -> None:
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

    def _check_setting_cam(self) -> None:

        if not self._get_setting_cam():
            showDialog(
                QMessageBox.Warning,
                "Камеры не настроины",
                "Настройте камеры \nНастройки -> Настройки камеры"
            )

    def _init_push_btn_action(self) -> None:
        self.btn_start_cam_photo.clicked.connect(
            self._start_cam_photo
        )

        self.btn_start_cam_pasport.clicked.connect(
            self._start_cam_pasport
        )

        self.capturePhoto.clicked.connect(
            self._take_image_face
        )

        self.capturePasport.clicked.connect(
            self._take_image_pasport
        )

        self.btn_save.clicked.connect(self._save)
        self.btn_clear.clicked.connect(self._clear)
        self.btn_print.clicked.connect(self._print)

    @Slot()
    def _show_personal_window(self) -> None:
        ListPersonal(self).show()

    @Slot()
    def _show_place_window(self) -> None:
        ListPlace(self).show()

    @Slot()
    def _show_setting_cam_window(self) -> None:
        SettingCam(self).show()

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

    def _get_setting_cam(self) -> bool | list:
        with connect() as conn:
            cams = conn.execute(
                cam_setting.select()
            ).all()

            if not cams or len(cams) != 2:
                return False
            else:
                return cams

    def _init_photo(self) -> None:
        load_image(self.imagePhoto, NO_MEDIA_IMAGE)
        load_image(self.imagePasport, NO_MEDIA_IMAGE)

    @Slot()
    def _start_cam_photo(self) -> None:
        cams = self._get_setting_cam()

        if cams:
            if self.stacked_widget_photo.currentIndex() == INDEX_PHOTO:
                self.stacked_widget_photo.setCurrentIndex(INDEX_CAMERA)
                self.face_wwc = WorkWithCam(
                    self.face_video_widget,
                    cams[0].selected_cam
                )

                self.face_wwc.start_cam()
            else:
                self.face_wwc.stop_cam()
                del self.face_wwc

                self.stacked_widget_photo.setCurrentIndex(INDEX_PHOTO)

    @Slot()
    def _start_cam_pasport(self) -> None:
        cams = self._get_setting_cam()

        if cams:
            if self.stacked_widget_pasport.currentIndex() == INDEX_PHOTO:
                self.stacked_widget_pasport.setCurrentIndex(INDEX_CAMERA)
                self.pasport_wwc = WorkWithCam(
                    self.pasport_video_widget,
                    cams[1].selected_cam
                )

                self.pasport_wwc.start_cam()
            else:
                self.pasport_wwc.stop_cam()
                del self.pasport_wwc

                self.stacked_widget_pasport.setCurrentIndex(INDEX_PHOTO)

    @Slot()
    def _take_image_face(self):
        if hasattr(self, "face_wwc"):
            self.face_file_name = self.face_wwc.get_filename()
            self.face_wwc._current_preview = QImage()
            self.face_wwc._image_capture.captureToFile(self.face_file_name)

            self.stacked_widget_photo.setCurrentIndex(INDEX_PHOTO)
            del_wwc(self.face_wwc, 1)
            load_image(self.imagePhoto, self.face_file_name)

    @Slot()
    def _take_image_pasport(self):
        if hasattr(self, "pasport_wwc"):
            self.pasport_file_name = self.pasport_wwc.get_filename()
            self.pasport_wwc._current_preview = QImage()
            self.pasport_wwc._image_capture.captureToFile(
                self.pasport_file_name)

            self.stacked_widget_pasport.setCurrentIndex(INDEX_PHOTO)
            del_wwc(self.pasport_wwc, 1)
            load_image(self.imagePasport, self.pasport_file_name)

    @Slot()
    def _print(self) -> None:
        if not hasattr(self, "data_propusk"):
            self._save()

        propusk_data = self.data_propusk.copy()

        propusk_data["personal"] = self.personal_combobox.currentText()
        propusk_data["place"] = self.place_combobox.currentIndex()

        Printer(
            str(TemplatePropusk(self.data_propusk,
                                os.path.join(ABSOLUTE_PATH, 'docs')
                                ))
        ).print()

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
            "face_photo": F"file://{self.face_file_name}",
            "pasport_photo": F"file://{self.pasport_file_name}"
        }

        with connect() as conn:
            conn.execute(
                list_propusk.insert().values(**self.data_propusk)
            )

    def _set_default_data(self):
        self.number_propusk.clear()
        self.date_from.setDate(QDate().currentDate())
        self.date_to.setDate(QDate().currentDate())
        self._init_photo()
        self.receiving_man.clear()
        self.purpose_visite.clear()
        
        if hasattr(self, "pasport_wwc", 1):
            del_wwc(self.pasport_wwc)
            self.stacked_widget_pasport.setCurrentIndex(INDEX_PHOTO)
            
        if hasattr(self, "face_wwc", 1):
            del_wwc(self.face_wwc)
            self.stacked_widget_photo.setCurrentIndex(INDEX_PHOTO)


def del_wwc(wwc: WorkWithCam, second: int = 0) -> None:
    sleep(second)
    wwc.stop_cam()
    del wwc
