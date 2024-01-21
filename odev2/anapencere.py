import sys
import mysql.connector
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QStatusBar
from PySide6.QtCore import QTimer
from ui_form import Ui_anapencere
from ui_formPerson import Ui_addPerson
from ui_formBul import Ui_Bul
from ui_formBilgi import Ui_Bilgi
from ui_formKira import Ui_Kira
from ui_plakasorgu import ui_plakasorgu


class anapencere(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_anapencere()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.statusBar = QStatusBar()

        self.sqlBaglan()
        self.dbCheck()
        self.tableCheck()

        self.ui.musteribilgi.clicked.connect(self.openPerson)
        self.ui.aracbilgi.clicked.connect(self.openBul)
        self.ui.aracbilgi2.clicked.connect(self.openBilgi)
        self.ui.aracbilgi3.clicked.connect(self.openKira)
        self.ui.aracbilgi_plaka.clicked.connect(self.openPlaka)

    def openPerson(self):
        self.w = addPerson(self, self.mycursor)
        self.w.show()

    def openBul(self):
        self.w = Bul(self, self.mycursor)
        self.w.show()

    def openBilgi(self):
        self.w = Bilgi(self, self.mycursor)
        self.w.show()

    def openKira(self):
        self.w = Kira(self, self.mycursor)
        self.w.show()

    def openPlaka(self):
        self.w = plakasorgu(self, self.mycursor)
        self.w.show()



    def sqlBaglan(self):
        self.dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3308"
        )

    def dbCheck(self):
        if self.dbConn.is_connected:
            self.mycursor = self.dbConn.cursor()
        self.target_db = "aracKiralama"
        try:
            self.mycursor.execute(f"USE {self.target_db}")
        except:
            self.mycursor.execute(f"CREATE DATABASE {self.target_db}")

    def tableCheck(self):
        self.mycursor.execute(f"USE {self.target_db}")
        self.mycursor.execute("SHOW tables")
        dbTable = [dbTbl[0] for dbTbl in self.mycursor.fetchall()]
        if dbTable == []:
            if 'musteriler' not in dbTable:
                self.mycursor.execute("""
                    CREATE TABLE musteriler(
                        userID int(10) PRIMARY KEY AUTO_INCREMENT,
                        ad varchar(50) NOT NULL,
                        soyad varchar(50) NOT NULL,
                        tcNO varchar(11) NOT NULL,
                        telNO varchar(15) NOT NULL,
                        dTarihi varchar(15) NOT NULL,
                        adres varchar(50) NOT NULL,
                        meslek varchar(50) NOT NULL,
                        ehliyetSınıfı varchar(50) NOT NULL,
                        medeniDurumu varchar(50) NOT NULL,
                        egitimDurumu varchar(50) NOT NULL
                    );
                """)
            if 'araclar' not in dbTable:
                self.mycursor.execute("""
                    CREATE TABLE araclar(
                        aracID int(10) PRIMARY KEY AUTO_INCREMENT,
                        aracTuru varchar(50) NOT NULL,
                        marka varchar(50) NOT NULL,
                        model varchar(50) NOT NULL,
                        uretimYil int(25) NOT NULL,
                        yakitTürü varchar(15) NOT NULL,
                        vites varchar(15) NOT NULL,
                        kasaTipi varchar(50) NOT NULL,
                        motorHacmi int(30) NOT NULL,
                        cekis varchar(50) NOT NULL,
                        kapı varchar(50) NOT NULL,
                        renk varchar(50) NOT NULL,
                        motorNo int(15) NOT NULL,
                        plaka varchar(50) NOT NULL
                    );
                """)
            if 'bilgi' not in dbTable:
                self.mycursor.execute("""
                    CREATE TABLE bilgi(
                        userID int(10) NOT NULL,
                        plaka varchar(50) NOT NULL,
                        yolculukNereye varchar(50) NOT NULL,
                        kaçGünKira varchar(50) NOT NULL
                    );
                """)
    def closeEvent(self, event):
        self.mycursor.close()
        self.dbConn.close()


class addPerson(QMainWindow):
    def __init__(self, mainWindow, mycursor, parent=None):
        super().__init__(parent)
        self.ui = Ui_addPerson()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.status_Bar = self.statusBar()
        self.mainWindow = mainWindow
        self.mycursor = mycursor
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["userID", "Ad", "Soyad", "telno", "dTarihi", "adres", "meslek", "ehliyetSınıfı", "egitimDurumu", "tcno",
             "medeniDurumu"])
        self.ui.tableWidget.setColumnWidth(0, 90)
        self.ui.tableWidget.setColumnWidth(1, 90)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 150)
        self.ui.tableWidget.setColumnWidth(5, 140)
        self.ui.tableWidget.setColumnWidth(6, 100)
        self.ui.tableWidget.setColumnWidth(7, 100)
        self.ui.tableWidget.setColumnWidth(8, 100)
        self.ui.tableWidget.setColumnWidth(9, 100)
        self.ui.tableWidget.setColumnWidth(10, 100)
        self.ui.tableWidget.setColumnWidth(11, 100)
        self.ui.pushButton_yeni.clicked.connect(self.yeniFonk)
        self.ui.pushButton_sil.clicked.connect(self.silFonk)
        self.ui.pushButton_update.clicked.connect(self.updateFonk)
        self.ui.pushButton_kaydet.clicked.connect(self.kaydetFonk)
        self.ui.tableWidget.cellDoubleClicked.connect(self.getInfoFonk)
        self.ui.tableWidget.cellChanged.connect(self.cellChangedFonk)
        self.ui.pushButton_Getir2.clicked.connect(self.getir)
        self.getir()

    def getir(self):
        # Fetch data from the database
        self.mycursor.execute("SELECT * FROM musteriler")
        rows = self.mycursor.fetchall()

        # Clear existing table
        self.ui.tableWidget.clearContents()

        # Set row and column count
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

        # Populate the table with data
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)


    def yeniFonk(self):
        self.ui.lineEdit_id.setText("")
        self.ui.lineEdit_ad.setText("")
        self.ui.lineEdit_soyad.setText("")
        self.ui.lineEdit_telno.setText("")
        self.ui.lineEdit_adres.setText("")
        self.ui.lineEdit_dTarihi.setText("")
        self.ui.lineEdit_tcno.setText("")
        self.ui.lineEdit_meslek.setText("")
        self.ui.lineEdit_ehliyet.setText("")
        self.ui.lineEdit_medeni.setText("")
        self.ui.lineEdit_egitim.setText("")
        self.ui.pushButton_sil.setEnabled(False)
        self.ui.pushButton_update.setEnabled(False)

    def silFonk(self):
        result = self.mesaj("Bir kaydı silmek üzeresiniz. Emin misiniz?")
        if result == QMessageBox.Yes:
            id = int(self.ui.lineEdit_id.text())
            self.mycursor.execute(f"""
                DELETE FROM `{self.mainWindow.target_db}`.`musteriler`
                WHERE (`userID` = '{id}');
            """)
            self.ui.pushButton_sil.setEnabled(False)
            self.mainWindow.dbConn.commit()
        else:
            self.status_Bar.showMessage("Silme iptal edildi", 5000)
        self.getir()

    def updateFonk(self):
        userID = self.ui.lineEdit_id.text()
        ad = self.ui.lineEdit_ad.text()
        soyad = self.ui.lineEdit_soyad.text()
        telno = self.ui.lineEdit_telno.text()
        adres = self.ui.lineEdit_adres.text()
        tcno = self.ui.lineEdit_tcno.text()
        dTarihi = self.ui.lineEdit_dTarihi.text()
        ehliyet = self.ui.lineEdit_ehliyet.text()
        meslek = self.ui.lineEdit_meslek.text()
        medeni = self.ui.lineEdit_medeni.text()
        egitim = self.ui.lineEdit_egitim.text()

        self.mycursor.execute(f"""
            UPDATE {self.mainWindow.target_db}.musteriler SET
            ad='{ad}',
            soyad='{soyad}',
            telno='{telno}',
            adres='{adres}',
            tcno='{tcno}',
            dTarihi='{dTarihi}',
            ehliyetSınıfı='{ehliyet}',
            meslek='{meslek}',
            medeniDurumu='{medeni}',
            egitimDurumu='{egitim}'
           WHERE userID='{userID}'
        """)

    def kaydetFonk(self):
        record_id = self.ui.lineEdit_id.text()
        if record_id != "":
            self.mycursor.execute(
                f"SELECT * FROM `{self.mainWindow.target_db}`.`musteriler` WHERE `userID` = '{record_id}'")
            existing_record = self.mycursor.fetchone()
            if existing_record is not None:
                result = self.mesaj("Bu kayıt mevcut. Güncelleme yapmak istiyor musunuz?")
                if result == QMessageBox.Yes:
                    self.updateFonk()
            else:
                self.status_Bar.showMessage("Kayıt bulunamadı", 5000)
        else:
            self.sql = """
                INSERT INTO musteriler(ad, soyad, telNO, tcNO, dTarihi, adres, meslek, ehliyetSınıfı, medeniDurumu, egitimDurumu)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.veri = (
                self.ui.lineEdit_ad.text(),
                self.ui.lineEdit_soyad.text(),
                self.ui.lineEdit_telno.text(),
                self.ui.lineEdit_tcno.text(),
                self.ui.lineEdit_dTarihi.text(),
                self.ui.lineEdit_adres.text(),
                self.ui.lineEdit_meslek.text(),
                self.ui.lineEdit_ehliyet.text(),
                self.ui.lineEdit_medeni.text(),
                self.ui.lineEdit_egitim.text()
            )
            self.mainWindow.mycursor.execute(self.sql, self.veri)
            self.mainWindow.dbConn.commit()
            self.status_Bar.showMessage("Kaydetme işlemi gerçekleşti", 5000)
        self.getir()

    def getInfoFonk(self):
        self.ui.pushButton_update.setEnabled(True)
        self.ui.pushButton_sil.setEnabled(True)
        self.cellChangedFonk()

    def cellChangedFonk(self, rowSec):
        if rowSec >= 0:
            self.ui.lineEdit_id.setText(str(self.ui.tableWidget.item(rowSec, 0).text() if self.ui.tableWidget.item(rowSec, 0) is not None else ""))
            self.ui.lineEdit_ad.setText(str(self.ui.tableWidget.item(rowSec, 1).text() if self.ui.tableWidget.item(rowSec, 1) is not None else ""))
            self.ui.lineEdit_soyad.setText(str(self.ui.tableWidget.item(rowSec, 2).text() if self.ui.tableWidget.item(rowSec, 2) is not None else ""))
            self.ui.lineEdit_telno.setText(str(self.ui.tableWidget.item(rowSec, 3).text() if self.ui.tableWidget.item(rowSec, 3) is not None else ""))
            self.ui.lineEdit_adres.setText(str(self.ui.tableWidget.item(rowSec, 4).text() if self.ui.tableWidget.item(rowSec, 4) is not None else ""))
            self.ui.lineEdit_tcno.setText(str(self.ui.tableWidget.item(rowSec, 5).text() if self.ui.tableWidget.item(rowSec, 5) is not None else ""))
            self.ui.lineEdit_dTarihi.setText(str(self.ui.tableWidget.item(rowSec, 6).text() if self.ui.tableWidget.item(rowSec, 6) is not None else ""))
            self.ui.lineEdit_ehliyet.setText(str(self.ui.tableWidget.item(rowSec, 7).text() if self.ui.tableWidget.item(rowSec, 7) is not None else ""))
            self.ui.lineEdit_meslek.setText(str(self.ui.tableWidget.item(rowSec, 8).text() if self.ui.tableWidget.item(rowSec, 8) is not None else ""))
            self.ui.lineEdit_medeni.setText(str(self.ui.tableWidget.item(rowSec, 9).text() if self.ui.tableWidget.item(rowSec, 9) is not None else ""))
            self.ui.lineEdit_egitim.setText(str(self.ui.tableWidget.item(rowSec, 10).text() if self.ui.tableWidget.item(rowSec, 10) is not None else ""))


    def mesaj(self, metin):
        self.message_box = QMessageBox()
        self.message_box.setText(metin)
        self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.message_box.setDefaultButton(QMessageBox.Cancel)
        return (self.message_box.exec())
class Bul(QMainWindow):
    def __init__(self, mainWindow, mycursor, parent=None):
        super().__init__(parent)
        self.ui = Ui_Bul()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.mainWindow = mainWindow
        self.mycursor = mycursor
        self.status_Bar = self.statusBar()
        self.getir()

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["aracTuru", "marka", "model", "uretimYil", "yakıtTürü", "vites", "kasaTipi", "motorHacmi", "cekis",
             "kapı", "renk", "motorNo"])
        self.ui.tableWidget.setColumnWidth(0, 90)
        self.ui.tableWidget.setColumnWidth(1, 90)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 150)
        self.ui.tableWidget.setColumnWidth(5, 140)
        self.ui.tableWidget.setColumnWidth(6, 100)
        self.ui.tableWidget.setColumnWidth(7, 100)
        self.ui.tableWidget.setColumnWidth(8, 100)
        self.ui.tableWidget.setColumnWidth(9, 100)
        self.ui.tableWidget.setColumnWidth(10, 100)
        self.ui.tableWidget.setColumnWidth(11, 100)
        self.ui.pushButton_yeni1.clicked.connect(self.yeniFonk1)
        self.ui.pushButton_sil1.clicked.connect(self.silFonk1)
        self.ui.pushButton_update1.clicked.connect(self.updateFonk1)
        self.ui.pushButton_kaydet1.clicked.connect(self.kaydetFonk1)
        self.ui.tableWidget.cellDoubleClicked.connect(self.getInfoFonk1)
        self.ui.tableWidget.cellChanged.connect(self.cellChangedFonk1)
        self.ui.pushButton_getir1.clicked.connect(self.getir)


    def getir(self):
        # Fetch data from the database
        self.mycursor.execute("SELECT * FROM araclar")
        rows = self.mycursor.fetchall()

        # Clear existing table
        self.ui.tableWidget.clearContents()

        # Set row and column count
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

        # Populate the table with data
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)


    def yeniFonk1(self):
        self.ui.lineEdit_aracTuru.setText("")
        self.ui.lineEdit_marka.setText("")
        self.ui.lineEdit_model.setText("")
        self.ui.lineEdit_uretimYil.setText("")
        self.ui.lineEdit_yakit.setText("")
        self.ui.lineEdit_vites.setText("")
        self.ui.lineEdit_kasa.setText("")
        self.ui.lineEdit_motorHacmi.setText("")
        self.ui.lineEdit_cekis.setText("")
        self.ui.lineEdit_kapi.setText("")
        self.ui.lineEdit_renk.setText("")
        self.ui.lineEdit_motor.setText("")
        self.ui.lineEdit_plaka.setText("")
        self.ui.pushButton_sil1.setEnabled(False)
        self.ui.pushButton_update1.setEnabled(False)

    def silFonk1(self):
        result = self.mesaj("Bir kaydı silmek üzeresiniz. Emin misiniz?")
        if result == QMessageBox.Yes:
            try:
                id = int(self.ui.lineEdit_aracid.text())
                self.mycursor.execute(f"""
                    DELETE FROM '{self.mainWindow.target_db}'.'araclar'
                    WHERE ('aracID' = '{id}');
                """)
                self.ui.pushButton_sil.setEnabled(False)
                self.mainWindow.dbConn.commit()
            except ValueError:
                # Handle the case where the entered value is not a valid integer
                self.status_Bar.showMessage("Geçersiz ID. Silme iptal edildi", 5000)
        else:
            self.status_Bar.showMessage("Silme iptal edildi", 5000)


    def updateFonk1(self):
        aracTuru = self.ui.lineEdit_aracTuru.text()
        marka = self.ui.lineEdit_marka.text()
        model = self.ui.lineEdit_model.text()
        uretimYil = self.ui.lineEdit_uretimYil.text()
        yakit = self.ui.lineEdit_yakit.text()
        vites = self.ui.lineEdit_vites.text()
        kasa_tipi = self.ui.lineEdit_kasa.text()
        motor_hacmi = self.ui.lineEdit_motorHacmi.text()
        cekis = self.ui.lineEdit_cekis.text()
        kapi = self.ui.lineEdit_kapi.text()
        renk = self.ui.lineEdit_renk.text()
        plaka = self.ui.lineEdit_plaka.text()
        self.mycursor.execute(f"""
            UPDATE {self.mainWindow.target_db}.araclar SET
            aracTuru='{aracTuru}',
            marka='{marka}',
            model='{model}',
            uretimYil='{uretimYil}',
            yakitTuru='{yakit}',
            vites='{vites}',
            kasaTipi='{kasa_tipi}',
            motorHacmi='{motor_hacmi}',
            cekis='{cekis}',
            kapı='{kapi}',
            renk='{renk}',
            plaka='{plaka}'
        """)
    def kaydetFonk1(self):
        record_id = self.ui.lineEdit_aracid.text()
        if record_id !="":
            self.mycursor.execute(
                f"SELECT * FROM '{self.mainWindow.target_db}'.'araclar' WHERE 'aracID' ='{record_id}'")
            existing_record = self.mycursor.fetchone()
            if existing_record is not None:
                result = self.mesaj("Bu kayıt mevcut.Güncelleme yapmak istiyor musunuz?")
                if result == QMessageBox.Yes:
                    self.uptadeFonk1()
            else:
                self.status_Bar.showMessage("Kayıt Bulunamadı",5000)
        else:
            self.sql = """
               INSERT INTO araclar(aracTuru,marka,model,uretimYil,yakitTürü,vites,kasaTipi,motorHacmi,cekis,kapı,renk,motorNo,plaka)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            self.veria = (
                self.ui.lineEdit_aracTuru.text(),
                self.ui.lineEdit_marka.text(),
                self.ui.lineEdit_model.text(),
                self.ui.lineEdit_uretimYil.text(),
                self.ui.lineEdit_yakit.text(),
                self.ui.lineEdit_vites.text(),
                self.ui.lineEdit_kasa.text(),
                self.ui.lineEdit_motorHacmi.text(),
                self.ui.lineEdit_cekis.text(),
                self.ui.lineEdit_kapi.text(),
                self.ui.lineEdit_renk.text(),
                self.ui.lineEdit_motor.text(),
                self.ui.lineEdit_plaka.text(),
            )
            self.mainWindow.mycursor.execute(self.sql,self.veria)
            self.mainWindow.dbConn.commit()
            self.status_Bar.showMessage("Kaydetme işlemi gerçekleşti",5000)
        self.getir()




    def getInfoFonk1(self):
        self.ui.pushButton_update.setEnabled(True)
        self.ui.pushButton_sil.setEnabled(True)
        self.cellChangedFonk()
    def cellChangedFonk1(self, rowSec):
        if rowSec >= 0:
            self.ui.lineEdit_aracTuru.setText(str(self.ui.tableWidget.item(rowSec, 0).text() if self.ui.tableWidget.item(rowSec, 0) is not None else ""))
            self.ui.lineEdit_marka.setText(str(self.ui.tableWidget.item(rowSec, 1).text() if self.ui.tableWidget.item(rowSec, 1) is not None else ""))
            self.ui.lineEdit_model.setText(str(self.ui.tableWidget.item(rowSec, 2).text() if self.ui.tableWidget.item(rowSec, 2) is not None else ""))
            self.ui.lineEdit_uretimYil.setText(str(self.ui.tableWidget.item(rowSec, 3).text() if self.ui.tableWidget.item(rowSec, 3) is not None else ""))
            self.ui.lineEdit_yakit.setText(str(self.ui.tableWidget.item(rowSec, 4).text() if self.ui.tableWidget.item(rowSec, 4) is not None else ""))
            self.ui.lineEdit_vites.setText(str(self.ui.tableWidget.item(rowSec, 5).text() if self.ui.tableWidget.item(rowSec, 5) is not None else ""))
            self.ui.lineEdit_kasa.setText(str(self.ui.tableWidget.item(rowSec, 6).text() if self.ui.tableWidget.item(rowSec, 6) is not None else ""))
            self.ui.lineEdit_motorHacmi.setText(str(self.ui.tableWidget.item(rowSec, 7).text() if self.ui.tableWidget.item(rowSec, 7) is not None else ""))
            self.ui.lineEdit_cekis.setText(str(self.ui.tableWidget.item(rowSec, 8).text() if self.ui.tableWidget.item(rowSec, 8) is not None else ""))
            self.ui.lineEdit_kapi.setText(str(self.ui.tableWidget.item(rowSec, 9).text() if self.ui.tableWidget.item(rowSec, 9) is not None else ""))
            self.ui.lineEdit_renk.setText(str(self.ui.tableWidget.item(rowSec, 10).text() if self.ui.tableWidget.item(rowSec, 10) is not None else ""))
            self.ui.lineEdit_motor.setText(str(self.ui.tableWidget.item(rowSec, 11).text() if self.ui.tableWidget.item(rowSec, 11) is not None else ""))
            self.ui.lineEdit_plaka.setText(str(self.ui.tableWidget.item(rowSec, 12).text() if self.ui.tableWidget.item(rowSec, 12) is not None else ""))



    def mesaj(self,metin):
        self.message_box=QMessageBox()
        self.message_box.setText(metin)
        self.message_box.setStandardButtons(QMessageBox.Yes |QMessageBox.Cancel)
        self.message_box.setDefaultButton(QMessageBox.Cancel)
        return(self.message_box.exec())


class Bilgi(QMainWindow):
    def __init__(self, mainWindow, mycursor, parent=None):
        super().__init__(parent)
        self.ui = Ui_Bilgi()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.mainWindow = mainWindow
        self.mycursor = mycursor
        self.ui.pushButton_2.clicked.connect(self.musteriBul)
        self.ui.pushButton.clicked.connect(self.aracBul)
        self.ui.pushButton_kirala.clicked.connect(self.kaydet)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["userID", "plaka", "ad", "soyad", "model", "marka", "yolculukNereye", "aracKaçGünKiralanıcak",])
        self.ui.tableWidget.setColumnWidth(0, 90)
        self.ui.tableWidget.setColumnWidth(1, 90)
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 150)
        self.ui.tableWidget.setColumnWidth(5, 140)
        self.ui.tableWidget.setColumnWidth(6, 100)
        self.ui.tableWidget.setColumnWidth(7, 100)
        self.kısabilgi()


    def kaydet(self):
        arac_id = self.ui.lineEdit_aracid.text()

        self.sql = """
            INSERT INTO bilgi(musteri_id,ad,soyad, arac_id,model,marka, yolculuk, kira)
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s)
        """
        self.veri = (
            self.ui.lineEdit_id.text(), self.ui.lineEdit_aracid.text(), self.ui.lineEdit_2.text(),
            self.ui.kira.text(),self.ui.lineEdit_ad.text(),self.ui.lineEdit_soyad.text(),self.ui.lineEdit_model.text(),self.ui.lineEdit_marka.text()
        )
        self.mainWindow.mycursor.execute(self.sql, self.veri)
        self.mainWindow.dbConn.commit()
        self.kısabilgi()



    def musteriBul(self):
        self.id=self.ui.lineEdit_id.text()
        self.mainWindow.mycursor.execute(f"""
        SELECT ad, soyad FROM musteriler
        WHERE userID = '{self.id}'
        """)
        result = self.mainWindow.mycursor.fetchone()
        if result:
            ad, soyad = result
            self.ui.lineEdit_ad.setText(ad)
            self.ui.lineEdit_soyad.setText(soyad)
        else:
            QMessageBox.warning(self, 'Müşteri Bulunamadı', 'Belirtilen ID Numarasına sahip müşteri bulunamadı.')

    def aracBul(self):
        self.aracid = self.ui.lineEdit_aracid.text()
        self.mainWindow.mycursor.execute(f"""
        SELECT marka, model FROM araclar
        WHERE aracid = '{self.aracid}'
        """)
        result = self.mainWindow.mycursor.fetchone()
        if result:
            marka, model = result
            self.ui.lineEdit_marka.setText(marka)
            self.ui.lineEdit_model.setText(model)
        else:
            QMessageBox.warning(self, 'Araç Bulunamadı', 'Belirtilen Plaka Numarasına sahip araç bulunamadı.')

    def kısabilgi(self):
        # Fetch data from the database
        self.mycursor.execute("SELECT ad,model,yolculuk,kira FROM bilgi")
        rows = self.mycursor.fetchall()

        # Clear existing table
        self.ui.tableWidget.clearContents()

        # Set row and column count
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

        # Populate the table with data
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)


class Kira(QMainWindow):
    def __init__(self, mainWindow, mycursor, parent=None):
        super().__init__(parent)
        self.ui = Ui_Kira()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.mainWindow = mainWindow
        self.mycursor = mycursor
        self.getir()

    def getir(self):
        # Fetch data from the database
        self.mycursor.execute("SELECT musteri_id,ad,soyad,arac_id,model,marka,yolculuk,kira FROM bilgi")
        rows = self.mycursor.fetchall()

        # Clear existing table
        self.ui.tableWidget.clearContents()

        # Set row and column count
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

        # Populate the table with data
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)


class plakasorgu(QMainWindow):
    def __init__(self, mainWindow, mycursor, parent=None):
        super().__init__(parent)
        self.ui = ui_plakasorgu()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.mainWindow = mainWindow
        self.mycursor = mycursor

        self.ui.pushButton_ara.clicked.connect(self.fonkPlaka)


    def fonkPlaka(self):
        self.plaka = self.ui.lineEdit_plaka.text()
        self.mainWindow.mycursor.execute(f"""
        SELECT * FROM araclar
        WHERE plaka = %s
        """, (self.plaka,))
        result = self.mainWindow.mycursor.fetchone()
        if result:
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setColumnCount(len(result))

            for j, value in enumerate(result):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(0, j, item)
        else:
            QMessageBox.warning(self, 'Araç Bulunamadı', 'Belirtilen Plaka Numarasına sahip araç bulunamadı.')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = anapencere()
    window.show()
    sys.exit(app.exec())
