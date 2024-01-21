# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formBul.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1203, 664)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 1201, 222))
        self.gridLayout_2 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_uretimYil = QLineEdit(self.formLayoutWidget)
        self.lineEdit_uretimYil.setObjectName(u"lineEdit_uretimYil")

        self.gridLayout_2.addWidget(self.lineEdit_uretimYil, 6, 1, 1, 1)

        self.label_20 = QLabel(self.formLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_20.setFont(font)

        self.gridLayout_2.addWidget(self.label_20, 6, 0, 1, 1)

        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_2.addWidget(self.label_16, 0, 3, 1, 1)

        self.lineEdit_cekis = QLineEdit(self.formLayoutWidget)
        self.lineEdit_cekis.setObjectName(u"lineEdit_cekis")

        self.gridLayout_2.addWidget(self.lineEdit_cekis, 5, 4, 1, 1)

        self.label_15 = QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_2.addWidget(self.label_15, 1, 3, 1, 1)

        self.label_24 = QLabel(self.formLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_2.addWidget(self.label_24, 5, 3, 1, 1)

        self.pushButton_sil1 = QPushButton(self.formLayoutWidget)
        self.pushButton_sil1.setObjectName(u"pushButton_sil1")

        self.gridLayout_2.addWidget(self.pushButton_sil1, 7, 5, 1, 1)

        self.label_23 = QLabel(self.formLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_2.addWidget(self.label_23, 6, 3, 1, 1)

        self.label_18 = QLabel(self.formLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_22 = QLabel(self.formLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.gridLayout_2.addWidget(self.label_22, 7, 0, 1, 1)

        self.lineEdit_yakit = QLineEdit(self.formLayoutWidget)
        self.lineEdit_yakit.setObjectName(u"lineEdit_yakit")

        self.gridLayout_2.addWidget(self.lineEdit_yakit, 7, 1, 1, 1)

        self.label_21 = QLabel(self.formLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_2.addWidget(self.label_21, 7, 3, 1, 1)

        self.lineEdit_aracid = QLineEdit(self.formLayoutWidget)
        self.lineEdit_aracid.setObjectName(u"lineEdit_aracid")
        self.lineEdit_aracid.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit_aracid, 1, 2, 1, 1)

        self.lineEdit_vites = QLineEdit(self.formLayoutWidget)
        self.lineEdit_vites.setObjectName(u"lineEdit_vites")

        self.gridLayout_2.addWidget(self.lineEdit_vites, 8, 1, 1, 1)

        self.pushButton_update1 = QPushButton(self.formLayoutWidget)
        self.pushButton_update1.setObjectName(u"pushButton_update1")

        self.gridLayout_2.addWidget(self.pushButton_update1, 5, 5, 1, 1)

        self.label_17 = QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)

        self.pushButton_yeni1 = QPushButton(self.formLayoutWidget)
        self.pushButton_yeni1.setObjectName(u"pushButton_yeni1")

        self.gridLayout_2.addWidget(self.pushButton_yeni1, 1, 5, 1, 1)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)

        self.lineEdit_motorHacmi = QLineEdit(self.formLayoutWidget)
        self.lineEdit_motorHacmi.setObjectName(u"lineEdit_motorHacmi")

        self.gridLayout_2.addWidget(self.lineEdit_motorHacmi, 1, 4, 1, 1)

        self.label_19 = QLabel(self.formLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout_2.addWidget(self.label_19, 8, 3, 1, 1)

        self.label_25 = QLabel(self.formLayoutWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 1)

        self.lineEdit_aracTuru = QLineEdit(self.formLayoutWidget)
        self.lineEdit_aracTuru.setObjectName(u"lineEdit_aracTuru")

        self.gridLayout_2.addWidget(self.lineEdit_aracTuru, 0, 1, 1, 1)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 5, 2, 1, 1)

        self.lineEdit_renk = QLineEdit(self.formLayoutWidget)
        self.lineEdit_renk.setObjectName(u"lineEdit_renk")

        self.gridLayout_2.addWidget(self.lineEdit_renk, 7, 4, 1, 1)

        self.lineEdit_kapi = QLineEdit(self.formLayoutWidget)
        self.lineEdit_kapi.setObjectName(u"lineEdit_kapi")

        self.gridLayout_2.addWidget(self.lineEdit_kapi, 6, 4, 1, 1)

        self.pushButton_kaydet1 = QPushButton(self.formLayoutWidget)
        self.pushButton_kaydet1.setObjectName(u"pushButton_kaydet1")

        self.gridLayout_2.addWidget(self.pushButton_kaydet1, 6, 5, 1, 1)

        self.lineEdit_motor = QLineEdit(self.formLayoutWidget)
        self.lineEdit_motor.setObjectName(u"lineEdit_motor")

        self.gridLayout_2.addWidget(self.lineEdit_motor, 8, 4, 1, 1)

        self.lineEdit_plaka = QLineEdit(self.formLayoutWidget)
        self.lineEdit_plaka.setObjectName(u"lineEdit_plaka")

        self.gridLayout_2.addWidget(self.lineEdit_plaka, 7, 2, 1, 1)

        self.lineEdit_model = QLineEdit(self.formLayoutWidget)
        self.lineEdit_model.setObjectName(u"lineEdit_model")

        self.gridLayout_2.addWidget(self.lineEdit_model, 5, 1, 1, 1)

        self.lineEdit_kasa = QLineEdit(self.formLayoutWidget)
        self.lineEdit_kasa.setObjectName(u"lineEdit_kasa")

        self.gridLayout_2.addWidget(self.lineEdit_kasa, 0, 4, 1, 1)

        self.lineEdit_marka = QLineEdit(self.formLayoutWidget)
        self.lineEdit_marka.setObjectName(u"lineEdit_marka")

        self.gridLayout_2.addWidget(self.lineEdit_marka, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
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
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QRect(0, 220, 1201, 431))
        QWidget.setTabOrder(self.lineEdit_aracTuru, self.lineEdit_kasa)
        QWidget.setTabOrder(self.lineEdit_kasa, self.lineEdit_marka)
        QWidget.setTabOrder(self.lineEdit_marka, self.lineEdit_motorHacmi)
        QWidget.setTabOrder(self.lineEdit_motorHacmi, self.lineEdit_model)
        QWidget.setTabOrder(self.lineEdit_model, self.lineEdit_cekis)
        QWidget.setTabOrder(self.lineEdit_cekis, self.lineEdit_uretimYil)
        QWidget.setTabOrder(self.lineEdit_uretimYil, self.lineEdit_kapi)
        QWidget.setTabOrder(self.lineEdit_kapi, self.lineEdit_yakit)
        QWidget.setTabOrder(self.lineEdit_yakit, self.lineEdit_renk)
        QWidget.setTabOrder(self.lineEdit_renk, self.lineEdit_vites)
        QWidget.setTabOrder(self.lineEdit_vites, self.lineEdit_motor)
        QWidget.setTabOrder(self.lineEdit_motor, self.lineEdit_plaka)
        QWidget.setTabOrder(self.lineEdit_plaka, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton_kaydet1)
        QWidget.setTabOrder(self.pushButton_kaydet1, self.pushButton_update1)
        QWidget.setTabOrder(self.pushButton_update1, self.pushButton_yeni1)
        QWidget.setTabOrder(self.pushButton_yeni1, self.pushButton_sil1)
        QWidget.setTabOrder(self.pushButton_sil1, self.lineEdit_aracid)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Araclar", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u00dcretim Y\u0131l\u0131", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Kasa Tipi", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Motor Hacmi", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u00c7eki\u015f", None))
        self.pushButton_sil1.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Kap\u0131", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Model", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Yak\u0131t T\u00fcr\u00fc", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Renk", None))
        self.pushButton_update1.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Marka", None))
        self.pushButton_yeni1.setText(QCoreApplication.translate("Form", u"Yeni", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Vites", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Motor No", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Ara\u00e7 T\u00fcr\u00fc", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ARAC ID", None))
        self.label.setText(QCoreApplication.translate("Form", u"Plaka", None))
        self.pushButton_kaydet1.setText(QCoreApplication.translate("Form", u"Kaydet", None))
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
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"12", None));
    # retranslateUi

