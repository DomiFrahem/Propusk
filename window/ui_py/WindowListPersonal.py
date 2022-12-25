# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'WindowListPersonal.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QGridLayout, QGroupBox, QHBoxLayout,
                               QLabel, QLineEdit, QListWidget, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_WindowListPersonal(object):
    def setupUi(self, WindowListPersonal):
        if not WindowListPersonal.objectName():
            WindowListPersonal.setObjectName(u"WindowListPersonal")
            
        WindowListPersonal.resize(742, 472)
        self.centralwidget = QWidget(WindowListPersonal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_personal_widget = QListWidget(self.groupBox)
        self.list_personal_widget.setObjectName(u"list_personal_widget")

        self.gridLayout.addWidget(self.list_personal_widget, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lastname = QLineEdit(self.groupBox_2)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.lastname)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(
            50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.firstname = QLineEdit(self.groupBox_2)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_3.addWidget(self.firstname)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.middlename = QLineEdit(self.groupBox_2)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_4.addWidget(self.middlename)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save_personal = QPushButton(self.groupBox_2)
        self.btn_save_personal.setObjectName(u"btn_save_personal")

        self.horizontalLayout.addWidget(self.btn_save_personal)

        self.btn_update_personal = QPushButton(self.groupBox_2)
        self.btn_update_personal.setObjectName(u"btn_update_personal")

        self.horizontalLayout.addWidget(self.btn_update_personal)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_delete_personal = QPushButton(self.groupBox_2)
        self.btn_delete_personal.setObjectName(u"btn_delete_personal")

        self.verticalLayout.addWidget(self.btn_delete_personal)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        WindowListPersonal.setCentralWidget(self.centralwidget)

        self.retranslateUi(WindowListPersonal)

        QMetaObject.connectSlotsByName(WindowListPersonal)
    # setupUi

    def retranslateUi(self, WindowListPersonal):
        WindowListPersonal.setWindowTitle(QCoreApplication.translate(
            "WindowListPersonal", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "WindowListPersonal", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.groupBox_2.setTitle(QCoreApplication.translate(
            "WindowListPersonal", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate(
            "WindowListPersonal", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate(
            "WindowListPersonal", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate(
            "WindowListPersonal", u"\u041e\u0442\u0447\u0435\u0442\u0432\u043e", None))
        self.btn_save_personal.setText(QCoreApplication.translate(
            "WindowListPersonal", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_update_personal.setText(QCoreApplication.translate(
            "WindowListPersonal", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_delete_personal.setText(QCoreApplication.translate(
            "WindowListPersonal", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi
