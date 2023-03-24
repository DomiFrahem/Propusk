# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'DialogSettingCam.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QGroupBox, QPushButton)


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

        self.mode_list = QComboBox(self.groupBox)
        self.mode_list.setObjectName(u'mode_list')
        self.gridLayout_3.addWidget(self.mode_list, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.save_setting_cam = QPushButton(DialogSettingCam)
        self.save_setting_cam.setObjectName(u"save_setting_cam")

        self.gridLayout.addWidget(self.save_setting_cam, 1, 0, 1, 1)

        self.retranslateUi(DialogSettingCam)

        QMetaObject.connectSlotsByName(DialogSettingCam)
    # setupUi

    def retranslateUi(self, DialogSettingCam):

        DialogSettingCam.setWindowTitle(QCoreApplication.translate(
            "DialogSettingCam", u"Настройка камеры", None))

        self.mode_list.addItem('USB Camera', userData='video')
        self.mode_list.addItem('IP Camera', userData='snapshot')

        self.groupBox.setTitle(QCoreApplication.translate(
            "DialogSettingCam", u"\u0424\u043e\u0442\u043e \u043b\u0438\u0446\u0430", None))
        self.save_setting_cam.setText(QCoreApplication.translate(
            "DialogSettingCam", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi
