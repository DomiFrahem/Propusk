# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingCam.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QWidget)


class Ui_SettingCam(object):
    def setupUi(self, SettingCam):
        if not SettingCam.objectName():
            SettingCam.setObjectName(u"SettingCam")
        SettingCam.resize(640, 207)
        self.centralwidget = QWidget(SettingCam)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.face_list_cam = QComboBox(self.groupBox)
        self.face_list_cam.setObjectName(u"face_list_cam")

        self.gridLayout_3.addWidget(self.face_list_cam, 0, 0, 1, 1)

        self.cam_photo = QLabel(self.groupBox)
        self.cam_photo.setObjectName(u"cam_photo")

        self.gridLayout_3.addWidget(self.cam_photo, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chacked_cam_face = QPushButton(self.groupBox)
        self.chacked_cam_face.setObjectName(u"chacked_cam_face")

        self.horizontalLayout.addWidget(self.chacked_cam_face)

        self.stop_cam_face = QPushButton(self.groupBox)
        self.stop_cam_face.setObjectName(u"stop_cam_face")

        self.horizontalLayout.addWidget(self.stop_cam_face)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pasport_list_cam = QComboBox(self.groupBox_2)
        self.pasport_list_cam.setObjectName(u"pasport_list_cam")

        self.gridLayout_2.addWidget(self.pasport_list_cam, 0, 0, 1, 1)

        self.cam_pasport = QLabel(self.groupBox_2)
        self.cam_pasport.setObjectName(u"cam_pasport")

        self.gridLayout_2.addWidget(self.cam_pasport, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checked_cam_pasport = QPushButton(self.groupBox_2)
        self.checked_cam_pasport.setObjectName(u"checked_cam_pasport")

        self.horizontalLayout_2.addWidget(self.checked_cam_pasport)

        self.stop_cam_pasport = QPushButton(self.groupBox_2)
        self.stop_cam_pasport.setObjectName(u"stop_cam_pasport")

        self.horizontalLayout_2.addWidget(self.stop_cam_pasport)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.save_setting_cam = QPushButton(self.centralwidget)
        self.save_setting_cam.setObjectName(u"save_setting_cam")

        self.gridLayout.addWidget(self.save_setting_cam, 1, 0, 1, 1)

        SettingCam.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingCam)

        QMetaObject.connectSlotsByName(SettingCam)
    # setupUi

    def retranslateUi(self, SettingCam):
        SettingCam.setWindowTitle(QCoreApplication.translate("SettingCam", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingCam", u"\u0424\u043e\u0442\u043e \u043b\u0438\u0446\u0430", None))
        self.cam_photo.setText(QCoreApplication.translate("SettingCam", u"TextLabel", None))
        self.chacked_cam_face.setText(QCoreApplication.translate("SettingCam", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.stop_cam_face.setText(QCoreApplication.translate("SettingCam", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingCam", u"\u0424\u043e\u0442\u043e \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.cam_pasport.setText(QCoreApplication.translate("SettingCam", u"TextLabel", None))
        self.checked_cam_pasport.setText(QCoreApplication.translate("SettingCam", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.stop_cam_pasport.setText(QCoreApplication.translate("SettingCam", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.save_setting_cam.setText(QCoreApplication.translate("SettingCam", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

