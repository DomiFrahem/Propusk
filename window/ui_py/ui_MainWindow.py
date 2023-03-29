# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'MainWindow.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime,
                            QMetaObject, QRect, QSize, QTime, Qt)
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QComboBox, QDateTimeEdit,
                               QGridLayout, QGroupBox, QHBoxLayout, QLabel, QMenu, QMenuBar,
                               QPushButton, QSizePolicy, QSplitter, QStatusBar, QTextEdit, QVBoxLayout, QWidget)
from PropuskWidgets.PLineEdit import PLineEdit
from PropuskWidgets.PStackedWidget import PStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(920, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QSize(864, 430))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        # self.actionSave = QAction(MainWindow)
        # self.actionSave.setObjectName(u"actionSave")
        # self.actionLoad = QAction(MainWindow)
        # self.actionLoad.setObjectName(u"actionLoad")
        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(u"actionExit_2")
        self.setting_cam = QAction(MainWindow)
        self.setting_cam.setObjectName(u"setting_cam")
        self.btn_show_personal_window = QAction(MainWindow)
        self.btn_show_personal_window.setObjectName(
            u"btn_show_personal_window")
        self.btn_show_place_window = QAction(MainWindow)
        self.btn_show_place_window.setObjectName(u"btn_show_place_window")
        self.update_list = QAction(MainWindow)
        self.update_list.setObjectName(u"update_list")
        self.btn_show_about = QAction(MainWindow)
        self.btn_show_about.setObjectName(u"btn_show_about")
        self.exit = QAction(MainWindow)
        self.exit.setObjectName(u"exit")
        self.action_open_history = QAction(MainWindow)
        self.action_open_history.setObjectName(u"action_open_history")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(400, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.number_propusk = PLineEdit(self.groupBox)
        self.number_propusk.setObjectName(u"number_propusk")
        self.number_propusk.setMaxLength(32767)

        self.horizontalLayout.addWidget(self.number_propusk)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.date_from = QDateTimeEdit(self.groupBox)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setDateTime(
            QDateTime(QDate(1999, 12, 31), QTime(21, 0, 0)))
        self.date_from.setTimeSpec(Qt.UTC)

        self.horizontalLayout_2.addWidget(self.date_from)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.date_to = QDateTimeEdit(self.groupBox)
        self.date_to.setObjectName(u"date_to")

        self.horizontalLayout_3.addWidget(self.date_to)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.personal_combobox = QComboBox(self.groupBox)
        self.personal_combobox.setObjectName(u"personal_combobox")

        self.horizontalLayout_4.addWidget(self.personal_combobox)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.place_combobox = QComboBox(self.groupBox)
        self.place_combobox.setObjectName(u"place_combobox")

        self.horizontalLayout_5.addWidget(self.place_combobox)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.receiving_man = QTextEdit(self.groupBox)
        self.receiving_man.setObjectName(u"receiving_man")

        self.verticalLayout.addWidget(self.receiving_man)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.purpose_visite = QTextEdit(self.groupBox)
        self.purpose_visite.setObjectName(u"purpose_visite")

        self.verticalLayout_2.addWidget(self.purpose_visite)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        # self.stacked_widget = PStackedWidget(self.groupBox_2, mode)
        # self.stacked_widget.setObjectName(u'stacked_widget')
        # self.stacked_widget.setEnabled(True)
        # self.verticalLayout_4.addWidget(self.stacked_widget)

        self.splitter = QSplitter(self.groupBox_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.btn_start_cam_photo = QPushButton(self.splitter)
        self.btn_start_cam_photo.setObjectName(u"btn_start_cam_photo")
        self.splitter.addWidget(self.btn_start_cam_photo)
        self.capturePhoto = QPushButton(self.splitter)
        self.capturePhoto.setObjectName(u"capturePhoto")
        self.splitter.addWidget(self.capturePhoto)

        self.verticalLayout_4.addWidget(self.splitter)

        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 2)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(
            self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_clear, 1, 0, 1, 1)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(
            self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_save, 1, 1, 1, 1)

        self.btn_print = QPushButton(self.centralwidget)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(
            self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_print, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 23))
        self.menubar.setMouseTracking(True)
        self.menubar.setAcceptDrops(True)
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QMenu(self.menu)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menuFile.addSeparator()
        # self.menuFile.addAction(self.actionSave)
        # self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.btn_show_about)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit)
        self.menu.addAction(self.setting_cam)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu_3.addSeparator()
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.btn_show_personal_window)
        self.menu_3.addAction(self.btn_show_place_window)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.update_list)
        self.menu_2.addAction(self.action_open_history)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0439 \u043f\u0440\u043e\u043f\u0443\u0441\u043a", None))
        self.actionExit.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        # self.actionSave.setText(
        #     QCoreApplication.translate("MainWindow", u"Save", None))
        # self.actionLoad.setText(
        #     QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionExit_2.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        self.setting_cam.setText(QCoreApplication.translate(
            "MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.btn_show_personal_window.setText(QCoreApplication.translate(
            "MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.btn_show_place_window.setText(QCoreApplication.translate(
            "MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.update_list.setText(QCoreApplication.translate(
            "MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043a\u0438", None))
        self.btn_show_about.setText(QCoreApplication.translate(
            "MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.exit.setText(QCoreApplication.translate(
            "MainWindow", u"Exit", None))
        self.action_open_history.setText(QCoreApplication.translate(
            "MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u043e\u0432", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0439 \u043f\u0440\u043e\u043f\u0443\u0441\u043a \u2116:", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d\u0435 \u0434\u043e:", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u0412\u044b\u0434\u0430\u043b:", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u044e\u0449\u0438\u0439:", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"\u0426\u0435\u043b\u044c \u0432\u0438\u0437\u0438\u0442\u0430:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u0424\u043e\u0442\u043e", None))

        self.btn_start_cam_photo.setText(QCoreApplication.translate(
            "MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443", None))
        self.capturePhoto.setText(QCoreApplication.translate(
            "MainWindow", u"\u0421\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_clear.setText(QCoreApplication.translate(
            "MainWindow", u"\u041e\u0442\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.btn_save.setText(QCoreApplication.translate(
            "MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_print.setText(QCoreApplication.translate(
            "MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menu.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u041D\u0430\u0441\u0442\u0440\u043E\u0439\u043A\u0438", None))
        self.menu_3.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438", None))
        self.menu_2.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
    # retranslateUi
