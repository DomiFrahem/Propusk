from PySide6.QtWidgets import QStackedWidget, QWidget, QLabel, QGridLayout
from PySide6.QtMultimediaWidgets import QVideoWidget
from module.cam.USBCam import load_image
import os


class PStackedWidget(QStackedWidget):
    def __init__(self, parent=None, mode='video'):
        super(PStackedWidget, self).__init__(parent)
        self.__mode = mode

        self.__setup_image_stacked()
        self.__setup_video_stacked()
        self.set_default_image()

    def __setup_image_stacked(self) -> None:
        self.page_image = QWidget()
        self.page_image.setObjectName("page_image")

        self.layout_image = QGridLayout(self.page_image)
        self.layout_image.setObjectName("layout_image")

        self.image = QLabel(self.page_image)
        self.image.setObjectName("image")
        self.layout_image.addWidget(self.image, 0, 0, 0, 0)

        self.addWidget(self.page_image)

    def __setup_video_stacked(self) -> None:
        self.page_video = QWidget()
        self.page_video.setObjectName("page_video")

        self.layout_video = QGridLayout(self.page_video)
        self.layout_video.setObjectName("layout_video")

        if self.__mode == 'video':
            self.video = QVideoWidget(self.page_video)
        else:
            self.video = QLabel(self.page_video)

        self.video.setObjectName("video")
        self.layout_video.addWidget(self.video, 0, 0, 0, 0)

        self.addWidget(self.page_video)

    def set_default_image(self) -> None:
        load_image(self.image, os.environ.get("NO_MEDIA_IMAGE"))

    def to_image(self) -> None:
        self.setCurrentIndex(0)

    def to_video(self) -> None:
        self.setCurrentIndex(1)

    def cupture_image(self) -> None:
        if self.__mode == 'video':
            self.video = self.video.cupture_image(self.image)
        else:
            self.video = self.video.cupture_image(self.image)