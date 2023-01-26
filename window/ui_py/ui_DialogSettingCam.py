# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogSettingCam.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_DialogSettingCam(object):
    def setupUi(self, DialogSettingCam):
        if not DialogSettingCam.objectName():
            DialogSettingCam.setObjectName(u"DialogSettingCam")
        DialogSettingCam.resize(640, 480)
        self.gridLayout = QGridLayout(DialogSettingCam)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(DialogSettingCam)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.face_list_cam = QComboBox(self.groupBox)
        self.face_list_cam.setObjectName(u"face_list_cam")

        self.gridLayout_3.addWidget(self.face_list_cam, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chacked_cam_face = QPushButton(self.groupBox)
        self.chacked_cam_face.setObjectName(u"chacked_cam_face")

        self.horizontalLayout.addWidget(self.chacked_cam_face)

        self.stop_cam_face = QPushButton(self.groupBox)
        self.stop_cam_face.setObjectName(u"stop_cam_face")

        self.horizontalLayout.addWidget(self.stop_cam_face)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.image = QLabel(self.page_3)
        self.image.setObjectName(u"image")

        self.gridLayout_2.addWidget(self.image, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_4 = QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.video = QVideoWidget(self.page_4)
        self.video.setObjectName(u"video")

        self.gridLayout_4.addWidget(self.video, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.save_setting_cam = QPushButton(DialogSettingCam)
        self.save_setting_cam.setObjectName(u"save_setting_cam")

        self.gridLayout.addWidget(self.save_setting_cam, 1, 0, 1, 1)


        self.retranslateUi(DialogSettingCam)

        QMetaObject.connectSlotsByName(DialogSettingCam)
    # setupUi

    def retranslateUi(self, DialogSettingCam):
        DialogSettingCam.setWindowTitle(QCoreApplication.translate("DialogSettingCam", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogSettingCam", u"\u0424\u043e\u0442\u043e \u043b\u0438\u0446\u0430", None))
        self.chacked_cam_face.setText(QCoreApplication.translate("DialogSettingCam", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.stop_cam_face.setText(QCoreApplication.translate("DialogSettingCam", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.image.setText(QCoreApplication.translate("DialogSettingCam", u"TextLabel", None))
        self.save_setting_cam.setText(QCoreApplication.translate("DialogSettingCam", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

