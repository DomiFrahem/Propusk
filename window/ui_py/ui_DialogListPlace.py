# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogListPlace.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DialogListPlace(object):
    def setupUi(self, DialogListPlace):
        if not DialogListPlace.objectName():
            DialogListPlace.setObjectName(u"DialogListPlace")
        DialogListPlace.resize(640, 480)
        self.gridLayout_3 = QGridLayout(DialogListPlace)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(DialogListPlace)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_place_widget = QListWidget(self.groupBox)
        self.list_place_widget.setObjectName(u"list_place_widget")

        self.gridLayout.addWidget(self.list_place_widget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(DialogListPlace)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.line_name_place = QLineEdit(self.groupBox_2)
        self.line_name_place.setObjectName(u"line_name_place")
        self.line_name_place.setMinimumSize(QSize(250, 0))

        self.verticalLayout_3.addWidget(self.line_name_place)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save_place = QPushButton(self.groupBox_2)
        self.btn_save_place.setObjectName(u"btn_save_place")

        self.horizontalLayout.addWidget(self.btn_save_place)

        self.btn_update_place = QPushButton(self.groupBox_2)
        self.btn_update_place.setObjectName(u"btn_update_place")

        self.horizontalLayout.addWidget(self.btn_update_place)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_delete_place = QPushButton(self.groupBox_2)
        self.btn_delete_place.setObjectName(u"btn_delete_place")

        self.verticalLayout.addWidget(self.btn_delete_place)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.retranslateUi(DialogListPlace)

        QMetaObject.connectSlotsByName(DialogListPlace)
    # setupUi

    def retranslateUi(self, DialogListPlace):
        DialogListPlace.setWindowTitle(QCoreApplication.translate("DialogListPlace", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogListPlace", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043c\u0435\u0441\u0442 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogListPlace", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("DialogListPlace", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u0435\u0441\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.btn_save_place.setText(QCoreApplication.translate("DialogListPlace", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_update_place.setText(QCoreApplication.translate("DialogListPlace", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_delete_place.setText(QCoreApplication.translate("DialogListPlace", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

