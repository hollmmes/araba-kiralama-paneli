# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_anapencere(object):
    def setupUi(self, anapencere):
        if not anapencere.objectName():
            anapencere.setObjectName(u"anapencere")
        anapencere.resize(483, 335)
        self.centralwidget = QWidget(anapencere)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 100, 401, 168))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.aracbilgi = QPushButton(self.gridLayoutWidget)
        self.aracbilgi.setObjectName(u"aracbilgi")
        self.aracbilgi.setFont(font)

        self.gridLayout_2.addWidget(self.aracbilgi, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.aracbilgi2 = QPushButton(self.gridLayoutWidget)
        self.aracbilgi2.setObjectName(u"aracbilgi2")
        self.aracbilgi2.setFont(font)

        self.gridLayout_2.addWidget(self.aracbilgi2, 2, 1, 1, 1)

        self.musteribilgi = QPushButton(self.gridLayoutWidget)
        self.musteribilgi.setObjectName(u"musteribilgi")
        self.musteribilgi.setFont(font)

        self.gridLayout_2.addWidget(self.musteribilgi, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.aracbilgi3 = QPushButton(self.gridLayoutWidget)
        self.aracbilgi3.setObjectName(u"aracbilgi3")
        self.aracbilgi3.setFont(font)

        self.gridLayout_2.addWidget(self.aracbilgi3, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 431, 61))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        anapencere.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(anapencere)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 483, 21))
        anapencere.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(anapencere)
        self.statusbar.setObjectName(u"statusbar")
        anapencere.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.musteribilgi, self.aracbilgi)
        QWidget.setTabOrder(self.aracbilgi, self.aracbilgi2)
        QWidget.setTabOrder(self.aracbilgi2, self.aracbilgi3)

        self.retranslateUi(anapencere)

        QMetaObject.connectSlotsByName(anapencere)
    # setupUi

    def retranslateUi(self, anapencere):
        anapencere.setWindowTitle(QCoreApplication.translate("anapencere", u"anapencere", None))
        self.label_4.setText(QCoreApplication.translate("anapencere", u"Ara\u00e7 kiralama bilgileri", None))
        self.aracbilgi.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
        self.label_5.setText(QCoreApplication.translate("anapencere", u"Kirada olan ara\u00e7lar", None))
        self.aracbilgi2.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
        self.musteribilgi.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
        self.label_3.setText(QCoreApplication.translate("anapencere", u"Ara\u00e7 Bilgileri", None))
        self.aracbilgi3.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
        self.label_2.setText(QCoreApplication.translate("anapencere", u"M\u00fc\u015fteri Bilgileri", None))
        self.label.setText(QCoreApplication.translate("anapencere", u"Ara\u00e7 kiralama", None))
    # retranslateUi

