# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPerson.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_addPerson(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1092, 663)
        Form.setStyleSheet(u"background-color: rgb(121, 121, 121);")
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 1091, 222))
        self.gridLayout_2 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_adres = QLineEdit(self.formLayoutWidget)
        self.lineEdit_adres.setObjectName(u"lineEdit_adres")

        self.gridLayout_2.addWidget(self.lineEdit_adres, 7, 1, 1, 1)

        self.lineEdit_ehliyet = QLineEdit(self.formLayoutWidget)
        self.lineEdit_ehliyet.setObjectName(u"lineEdit_ehliyet")

        self.gridLayout_2.addWidget(self.lineEdit_ehliyet, 6, 4, 1, 1)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 6, 3, 1, 1)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)

        self.lineEdit_telno = QLineEdit(self.formLayoutWidget)
        self.lineEdit_telno.setObjectName(u"lineEdit_telno")

        self.gridLayout_2.addWidget(self.lineEdit_telno, 1, 4, 1, 1)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 7, 3, 1, 1)

        self.lineEdit_egitim = QLineEdit(self.formLayoutWidget)
        self.lineEdit_egitim.setObjectName(u"lineEdit_egitim")

        self.gridLayout_2.addWidget(self.lineEdit_egitim, 8, 4, 1, 1)

        self.lineEdit_id = QLineEdit(self.formLayoutWidget)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit_id, 0, 1, 1, 1)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.lineEdit_ad = QLineEdit(self.formLayoutWidget)
        self.lineEdit_ad.setObjectName(u"lineEdit_ad")

        self.gridLayout_2.addWidget(self.lineEdit_ad, 1, 1, 1, 1)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 5, 3, 1, 1)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.lineEdit_medeni = QLineEdit(self.formLayoutWidget)
        self.lineEdit_medeni.setObjectName(u"lineEdit_medeni")

        self.gridLayout_2.addWidget(self.lineEdit_medeni, 7, 4, 1, 1)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)

        self.lineEdit_tcno = QLineEdit(self.formLayoutWidget)
        self.lineEdit_tcno.setObjectName(u"lineEdit_tcno")

        self.gridLayout_2.addWidget(self.lineEdit_tcno, 5, 1, 1, 1)

        self.lineEdit_meslek = QLineEdit(self.formLayoutWidget)
        self.lineEdit_meslek.setObjectName(u"lineEdit_meslek")

        self.gridLayout_2.addWidget(self.lineEdit_meslek, 5, 4, 1, 1)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 8, 3, 1, 1)

        self.lineEdit_soyad = QLineEdit(self.formLayoutWidget)
        self.lineEdit_soyad.setObjectName(u"lineEdit_soyad")

        self.gridLayout_2.addWidget(self.lineEdit_soyad, 0, 4, 1, 1)

        self.lineEdit_dTarihi = QLineEdit(self.formLayoutWidget)
        self.lineEdit_dTarihi.setObjectName(u"lineEdit_dTarihi")

        self.gridLayout_2.addWidget(self.lineEdit_dTarihi, 6, 1, 1, 1)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.pushButton_sil = QPushButton(self.formLayoutWidget)
        self.pushButton_sil.setObjectName(u"pushButton_sil")

        self.gridLayout_2.addWidget(self.pushButton_sil, 7, 5, 1, 1)

        self.pushButton_kaydet = QPushButton(self.formLayoutWidget)
        self.pushButton_kaydet.setObjectName(u"pushButton_kaydet")

        self.gridLayout_2.addWidget(self.pushButton_kaydet, 6, 5, 1, 1)

        self.pushButton_update = QPushButton(self.formLayoutWidget)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.gridLayout_2.addWidget(self.pushButton_update, 5, 5, 1, 1)

        self.pushButton_yeni = QPushButton(self.formLayoutWidget)
        self.pushButton_yeni.setObjectName(u"pushButton_yeni")

        self.gridLayout_2.addWidget(self.pushButton_yeni, 1, 5, 1, 1)

        self.pushButton_Getir2 = QPushButton(self.formLayoutWidget)
        self.pushButton_Getir2.setObjectName(u"pushButton_Getir2")

        self.gridLayout_2.addWidget(self.pushButton_Getir2, 8, 5, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 220, 1091, 431))
        QWidget.setTabOrder(self.lineEdit_id, self.lineEdit_soyad)
        QWidget.setTabOrder(self.lineEdit_soyad, self.lineEdit_ad)
        QWidget.setTabOrder(self.lineEdit_ad, self.lineEdit_telno)
        QWidget.setTabOrder(self.lineEdit_telno, self.lineEdit_tcno)
        QWidget.setTabOrder(self.lineEdit_tcno, self.lineEdit_meslek)
        QWidget.setTabOrder(self.lineEdit_meslek, self.lineEdit_dTarihi)
        QWidget.setTabOrder(self.lineEdit_dTarihi, self.lineEdit_ehliyet)
        QWidget.setTabOrder(self.lineEdit_ehliyet, self.lineEdit_adres)
        QWidget.setTabOrder(self.lineEdit_adres, self.lineEdit_medeni)
        QWidget.setTabOrder(self.lineEdit_medeni, self.lineEdit_egitim)
        QWidget.setTabOrder(self.lineEdit_egitim, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton_sil)
        QWidget.setTabOrder(self.pushButton_sil, self.pushButton_kaydet)
        QWidget.setTabOrder(self.pushButton_kaydet, self.pushButton_update)
        QWidget.setTabOrder(self.pushButton_update, self.pushButton_yeni)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Ehliyet S\u0131n\u0131f\u0131", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Soyad", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Medeni Durum", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Do\u011fum Tarihi", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ad", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Adres", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Meslek", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tc Kimlik NO", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Tel No", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"E\u011fitim Durumu", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.pushButton_sil.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.pushButton_yeni.setText(QCoreApplication.translate("Form", u"Yeni", None))
        self.pushButton_Getir2.setText(QCoreApplication.translate("Form", u"Getir", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"7", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"8", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"9", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"11", None));
    # retranslateUi

