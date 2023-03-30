# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'DialogSettingCam.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (
    QComboBox, QPushButton, QTabWidget, QVBoxLayout, QWidget)


class Ui_DialogSettingCam(object):
    def setupUi(self, DialogSettingCam):
        if not DialogSettingCam.objectName():
            DialogSettingCam.setObjectName(u"DialogSettingCam")
        DialogSettingCam.resize(794, 559)
        self.verticalLayout_2 = QVBoxLayout(DialogSettingCam)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(DialogSettingCam)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.mode_list = QComboBox(self.tab)
        self.mode_list.setObjectName(u'mode_list')
        self.verticalLayout.addWidget(self.mode_list)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")

        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.save_setting_cam = QPushButton(DialogSettingCam)
        self.save_setting_cam.setObjectName(u"save_setting_cam")

        self.verticalLayout_2.addWidget(self.save_setting_cam)

        self.retranslateUi(DialogSettingCam)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DialogSettingCam)
    # setupUi

    def retranslateUi(self, DialogSettingCam):
        DialogSettingCam.setWindowTitle(QCoreApplication.translate(
            "DialogSettingCam", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043a\u0430\u043c\u0435\u0440\u044b", None))

        self.mode_list.addItem('USB Camera', userData='video')
        self.mode_list.addItem('IP Camera', userData='snapshot')
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate(
            "DialogSettingCam", u"\u041A\u0430\u043C\u0435\u0440\u0430 \u0434\u043B\u044F \u043B\u0438\u0446\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate(
            "DialogSettingCam", u"\u041A\u0430\u043C\u0435\u0440\u0430 \u0434\u043B\u044F \u0434\u043E\u043A\u0443\u043C\u0435\u043D\u0442\u0430", None))
        self.save_setting_cam.setText(QCoreApplication.translate(
            "DialogSettingCam", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi
