# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formBilgi.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(561, 411)
        Form.setStyleSheet(u"background-color: rgb(93, 93, 93);")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 561, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEdit_model = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_model.setObjectName(u"lineEdit_model")
        self.lineEdit_model.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_model, 2, 4, 1, 1)

        self.lineEdit_ad = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ad.setObjectName(u"lineEdit_ad")
        self.lineEdit_ad.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_ad, 2, 1, 1, 1)

        self.lineEdit_id = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.gridLayout.addWidget(self.lineEdit_id, 0, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_soyad = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_soyad.setObjectName(u"lineEdit_soyad")
        self.lineEdit_soyad.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_soyad, 3, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_aracid = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_aracid.setObjectName(u"lineEdit_aracid")

        self.gridLayout.addWidget(self.lineEdit_aracid, 0, 4, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)

        self.lineEdit_marka = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_marka.setObjectName(u"lineEdit_marka")
        self.lineEdit_marka.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_marka, 3, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 5, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 6, 1, 1)

        self.kira = QLineEdit(self.gridLayoutWidget)
        self.kira.setObjectName(u"kira")

        self.gridLayout.addWidget(self.kira, 2, 6, 1, 1)

        self.pushButton_kirala = QPushButton(self.gridLayoutWidget)
        self.pushButton_kirala.setObjectName(u"pushButton_kirala")
        self.pushButton_kirala.setFont(font)

        self.gridLayout.addWidget(self.pushButton_kirala, 3, 6, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 200, 561, 211))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Arac ID", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ad", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Marka", None))
        self.label.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Model", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Soyad", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Bul", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Bul", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Yolculuk Nereye", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Ara\u00e7 Ka\u00e7 G\u00fcn Kiralan\u0131cak", None))
        self.pushButton_kirala.setText(QCoreApplication.translate("Form", u"Kirala", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Yolculuk Nereye", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Ara\u00e7 Ka\u00e7 G\u00fcn Kiralan\u0131cak", None));
    # retranslateUi

