# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogAbout.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        if not DialogAbout.objectName():
            DialogAbout.setObjectName(u"DialogAbout")
        DialogAbout.resize(456, 295)
        self.verticalLayout = QVBoxLayout(DialogAbout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DialogAbout)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.version = QLabel(DialogAbout)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.version)

        self.verticalSpacer_2 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(DialogAbout)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(DialogAbout)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(400, 0))

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 67, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(DialogAbout)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(DialogAbout)

        QMetaObject.connectSlotsByName(DialogAbout)
    # setupUi

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(QCoreApplication.translate("DialogAbout", u"\u041e \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("DialogAbout", u"Propusk", None))
        self.version.setText(QCoreApplication.translate("DialogAbout", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("DialogAbout", u"Git:", None))
        self.label_4.setText(QCoreApplication.translate("DialogAbout", u"<a href=\"https://tj.kbsu.ru/AlexSidorov/propusk\">https://tj.kbsu.ru/AlexSidorov/propusk</a>", None))
        self.label_2.setText(QCoreApplication.translate("DialogAbout", u"@ KBSU", None))
    # retranslateUi

