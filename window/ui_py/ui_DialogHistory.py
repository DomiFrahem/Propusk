# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogHistory.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_DialogHistory(object):
    def setupUi(self, DialogHistory):
        if not DialogHistory.objectName():
            DialogHistory.setObjectName(u"DialogHistory")
        DialogHistory.resize(935, 543)
        self.horizontalLayout = QHBoxLayout(DialogHistory)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(DialogHistory)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_search = QLineEdit(self.groupBox)
        self.line_search.setObjectName(u"line_search")

        self.verticalLayout.addWidget(self.line_search)

        self.list_propusk = QListWidget(self.groupBox)
        self.list_propusk.setObjectName(u"list_propusk")

        self.verticalLayout.addWidget(self.list_propusk)


        self.horizontalLayout.addWidget(self.groupBox)

        self.browser = QTextBrowser(DialogHistory)
        self.browser.setObjectName(u"browser")

        self.horizontalLayout.addWidget(self.browser)


        self.retranslateUi(DialogHistory)

        QMetaObject.connectSlotsByName(DialogHistory)
    # setupUi

    def retranslateUi(self, DialogHistory):
        DialogHistory.setWindowTitle(QCoreApplication.translate("DialogHistory", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogHistory", u"\u0421\u043f\u0438\u0441\u043e\u043a", None))
    # retranslateUi

