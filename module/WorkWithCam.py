import sys
import os

from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel
from PySide6.QtMultimedia import (
    QMediaDevices, QCamera, QImageCapture, QMediaCaptureSession)
from appdirs import user_data_dir
from datetime import datetime

IMAGES_PATH = F"{user_data_dir()}/propusk/photo"

class WorkWithCam:
    def __init__(self, q_Video_Widget: QVideoWidget, index_cam: int = 0) -> None:
        self._create_dirs()
        
        self._capture_session = None
        self._camera = None
        self._camera_info = None
        self._image_capture = None
        self._video_widget = q_Video_Widget

        list_cam_device = QMediaDevices.videoInputs()
        if list_cam_device[index_cam]:
            self._camera_info = list_cam_device[index_cam]

        else:
            raise IndexError(
                f"Не нашли камеру QMediaDevices.videoInputs(). убидитесь, что у вас есть камера")

    def start_cam(self):
        self._camera = QCamera(self._camera_info)
        self._camera.errorOccurred.connect(self._camera_error)
        self._image_capture = QImageCapture(self._camera)
        self._image_capture.imageCaptured.connect(self.image_captured)
        self._image_capture.imageSaved.connect(self.image_saved)
        self._image_capture.errorOccurred.connect(self._capture_error)
        self._capture_session = QMediaCaptureSession()
        self._capture_session.setCamera(self._camera)
        self._capture_session.setImageCapture(self._image_capture)

        if self._camera and self._camera.error() == QCamera.NoError:
            # print()
            name = self._camera_info.description()
            self._capture_session.setVideoOutput(self._video_widget)
            self._camera.start()
        else:
            print("Camera unavailable")

    def stop_cam(self) -> None:
        if self._camera and self._camera.isActive():
            self._camera.stop()

    def __del__(self) -> None:
        self.stop_cam()


    @Slot(int, QImageCapture.Error, str)
    def _capture_error(self, id, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    @Slot(QCamera.Error, str)
    def _camera_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    @staticmethod
    def get_filename() -> str:
        return F"{IMAGES_PATH}/propusk_{datetime.now().timestamp()}.jpg"
        
    def _create_dirs(self):
        if not os.path.exists(IMAGES_PATH):
            os.mkdir(IMAGES_PATH)

    @Slot(int, QImage)
    def image_captured(self, id, previewImage):
        self._current_preview = previewImage

    @Slot(int, str)
    def image_saved(self, id, fileName):
        ...
        
    def show_status_message(self, message):
        print(message, 5000)


def load_image(qlabel: QLabel, path_file: str) -> None:
    qlabel.setPixmap(QPixmap(QImage(path_file)).scaled(
                qlabel.width(),
                qlabel.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.FastTransformation
            ))