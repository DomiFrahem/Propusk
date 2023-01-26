# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogCustomVariables.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DialogCustomVariables(object):
    def setupUi(self, DialogCustomVariables):
        if not DialogCustomVariables.objectName():
            DialogCustomVariables.setObjectName(u"DialogCustomVariables")
        DialogCustomVariables.resize(590, 228)
        DialogCustomVariables.setMinimumSize(QSize(590, 228))
        DialogCustomVariables.setMaximumSize(QSize(590, 228))
        self.verticalLayout = QVBoxLayout(DialogCustomVariables)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(DialogCustomVariables)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.path_photo = QLineEdit(self.groupBox)
        self.path_photo.setObjectName(u"path_photo")

        self.horizontalLayout.addWidget(self.path_photo)

        self.btn_show_path_photo = QPushButton(self.groupBox)
        self.btn_show_path_photo.setObjectName(u"btn_show_path_photo")

        self.horizontalLayout.addWidget(self.btn_show_path_photo)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(DialogCustomVariables)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.path_db = QLineEdit(self.groupBox_2)
        self.path_db.setObjectName(u"path_db")

        self.horizontalLayout_2.addWidget(self.path_db)

        self.btn_show_path_database = QPushButton(self.groupBox_2)
        self.btn_show_path_database.setObjectName(u"btn_show_path_database")

        self.horizontalLayout_2.addWidget(self.btn_show_path_database)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_save = QPushButton(DialogCustomVariables)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout.addWidget(self.btn_save)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(DialogCustomVariables)

        QMetaObject.connectSlotsByName(DialogCustomVariables)
    # setupUi

    def retranslateUi(self, DialogCustomVariables):
        DialogCustomVariables.setWindowTitle(QCoreApplication.translate("DialogCustomVariables", u"\u0418\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogCustomVariables", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f \u0441 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f\u043c\u0438", None))
        self.btn_show_path_photo.setText(QCoreApplication.translate("DialogCustomVariables", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0443\u0442\u044c \u043a \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogCustomVariables", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f \u0441 \u0431\u0430\u0437\u043e\u0439 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.btn_show_path_database.setText(QCoreApplication.translate("DialogCustomVariables", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0443\u0442\u044c \u043a \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438", None))
        self.btn_save.setText(QCoreApplication.translate("DialogCustomVariables", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

