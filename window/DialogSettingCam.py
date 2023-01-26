from .ui_py.ui_DialogSettingCam import Ui_DialogSettingCam
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Slot
from PySide6.QtMultimedia import QMediaDevices
from module.WorkWithCam import WorkWithCam, get_list_name_cam, load_image
from module.WorkWithDB import *

class SettingCam(QDialog, Ui_DialogSettingCam):
    def __init__(self, parent=None) -> None:
        super(SettingCam, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        
        self.load_cams()
        load_image(self.image, os.environ.get("NO_MEDIA_IMAGE"))      
        self.chacked_cam_face.clicked.connect(self._open_cam_face)
        self.stop_cam_face.clicked.connect(self._close_cam_face)
        self.save_setting_cam.clicked.connect(self._save_setting_cam)

    def load_cams(self) -> None:
        for name in get_list_name_cam():
            self.face_list_cam.addItem(name)
        self.load_cams_from_db()

    def _save_setting_cam(self) -> None:
        self.save_cams(self.face_list_cam.currentText())

    def _open_cam_face(self) -> None:
        self.stackedWidget.setCurrentIndex(int(os.environ.get('INDEX_CAMERA')))
        self._cam_face = WorkWithCam(
            self.video, self.face_list_cam.currentText())
        self._cam_face.start_cam()

    def _close_cam_face(self) -> None:
        if self._cam_face:
            self.stackedWidget.setCurrentIndex(int(os.environ.get('INDEX_PHOTO')))
        del self._cam_face

    def load_cams_from_db(self):
        with connect() as conn:
            result = conn.execute(cam_setting.select()).fetchone()
            if result:
                self.face_list_cam.setCurrentText(result.selected_cam)
                
    def save_cams(self, description_cam: str) -> None:
        query = None
        with connect() as conn:
            result = conn.execute(cam_setting.select()).fetchone()
            if result is None:
                query = cam_setting.insert().values(selected_cam=description_cam)
            else:
                query = cam_setting.update().where(
                    cam_setting.c.id == 1).values(selected_cam=description_cam)
            result = conn.execute(query)
