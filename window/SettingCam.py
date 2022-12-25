from .ui_py.SettingCam import Ui_SettingCam
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, Slot
from PySide6.QtMultimedia import QMediaDevices
from module.WorkWithCam import WorkWithCam
from module.WorkWithDB import *


class SettingCam(QMainWindow, Ui_SettingCam):
    def __init__(self, parent=None) -> None:
        super(SettingCam, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.load_cams()

        self.face_list_cam.currentTextChanged.connect(
            self.print_selected_face_cam)
        self.pasport_list_cam.currentTextChanged.connect(
            self.print_selected_pasport_cam)

        self.chacked_cam_face.clicked.connect(self._open_cam_face)
        self.stop_cam_face.clicked.connect(self._close_cam_face)

        self.checked_cam_pasport.clicked.connect(self._open_cam_pasport)
        self.stop_cam_pasport.clicked.connect(self._close_cam_pasport)

        self.save_setting_cam.clicked.connect(self._save_setting_cam)

    def load_cams(self) -> None:
        for device in list(QMediaDevices.videoInputs()):
            self.face_list_cam.addItem(device.description())
            self.pasport_list_cam.addItem(device.description())

        self.load_cams_from_db()

    @Slot()
    def _save_setting_cam(self) -> None:
        self.save_cams(1, self.face_list_cam.currentIndex())
        self.save_cams(2, self.pasport_list_cam.currentIndex())

    @Slot()
    def _open_cam_face(self) -> None:
        self.cam_photo.setHidden(False)
        self._cam_face = WorkWithCam(
            self.cam_photo, self.face_list_cam.currentIndex())
        self._cam_face.start_cam()

    @Slot()
    def _open_cam_pasport(self) -> None:
        self.cam_pasport.setHidden(False)
        self._cam_pasport = WorkWithCam(
            self.cam_pasport, self.pasport_list_cam.currentIndex())
        self._cam_pasport.start_cam()

    @Slot()
    def _close_cam_face(self) -> None:
        if self._cam_face:
            self._cam_face.stop_cam()
            self.cam_photo.setHidden(True)
            del (self._cam_face)

    @Slot()
    def _close_cam_pasport(self) -> None:
        if self._cam_pasport:
            self._cam_pasport.stop_cam()
            self.cam_pasport.setHidden(True)
            del (self._cam_pasport)

    @Slot()
    def print_selected_face_cam(self, value) -> None:
        print(F"face_list_cam selected item {value}")

    @Slot()
    def print_selected_pasport_cam(self, value) -> None:
        print(F"pasport_list_cam selected item {value}")

    def load_cams_from_db(self):
        with connect() as conn:
            result = conn.execute(cam_setting.select()).all()

            if result:
                self.face_list_cam.setCurrentIndex(result[0].selected_cam)
                self.pasport_list_cam.setCurrentIndex(result[1].selected_cam)

    def save_cams(self, index: int, index_cam: int) -> None:
        query = None
        with connect() as conn:
            select_cam = cam_setting.select().where(cam_setting.c.id == index)
            result = conn.execute(select_cam)
            if not result.all() or any([x for x in result if x.id in (1, 2)]):
                query = cam_setting.insert().values(selected_cam=index_cam)
            else:
                query = cam_setting.update().where(
                    cam_setting.c.id == index).values(selected_cam=index_cam)
            result = conn.execute(query)
