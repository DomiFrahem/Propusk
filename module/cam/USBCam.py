import os

from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel
from PySide6.QtMultimedia import (
    QMediaDevices, QCamera, QImageCapture, QMediaCaptureSession)
from itertools import groupby
from logger import logger
from module.ImageTool import create_filename

if not os.environ.get("PHOTO_DIR"):
    logger.error("Не задана локальная переменная PHOTO_DIR")
    raise ValueError(
        "не задана локальная переменная PHOTO_DIR"
    )


class USBCam:
    _capture_session: QMediaCaptureSession
    _camera: QCamera
    _camera_info: list[QMediaDevices]
    _image_capture: QImageCapture
    _current_preview = QImage()
    _label: QLabel
    
    def __init__(self, q_Video_Widget: QVideoWidget, name_cam: str) -> None:
        self._create_dirs()
        self._video_widget = q_Video_Widget

        self._camera_info = get_object_cam_by_name(name_cam)
        if not self._camera_info:
            logger.error("Не нашли камеру QMediaDevices.videoInputs(). убидитесь, что у вас есть камера")
            raise IndexError(
                "Не нашли камеру QMediaDevices.videoInputs(). убидитесь, что у вас есть камера")
        

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
            self._capture_session.setVideoOutput(self._video_widget)
            self._camera.start()
        else:
            logger.error("Camera unavailable")

    def stop_cam(self) -> None:
        try:
            if self._camera and self._camera.isActive():
                self._camera.stop()
        except RuntimeError as err:
            logger.error(err)

    def __del__(self) -> None:
        self.stop_cam()

    def cupture_image(self, label: QLabel) -> str:
        self._label = label
        self._file_name = create_filename()
        self._image_capture.captureToFile(self._file_name)
        logger.info(F"Создаем файл {self._file_name}")
        
        return self._file_name

    @Slot(int, QImageCapture.Error, str)
    def _capture_error(self, id, error, error_string):
        logger.error(error_string)

    @Slot(QCamera.Error, str)
    def _camera_error(self, error, error_string):
        logger.error(error_string)

    def _create_dirs(self):
        if not os.path.exists(os.environ.get('PHOTO_DIR')):
            os.mkdir(os.environ.get('PHOTO_DIR'))

    @Slot(int, QImage)
    def image_captured(self, id, previewImage):
        self._current_preview = previewImage

    @Slot(int, str)
    def image_saved(self, id, fileName):
       load_image(self._label, fileName)
       self.stop_cam()

        



def load_image(qlabel: QLabel, path_file: str) -> None:
    logger.info(F"Set image to label: {path_file}")
    qlabel.setPixmap(QPixmap(QImage(path_file)).scaled(
        qlabel.width()-4,
        qlabel.height(),
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.FastTransformation
    ))


def get_list_name_cam() -> list:
    return [x for x, _ in groupby(
        [x.description() for x in QMediaDevices.videoInputs()]
    )]

def get_object_cam_by_name(name_cam: str) -> QMediaDevices:
    return [x for x in QMediaDevices.videoInputs() if x.description() == name_cam][0]
