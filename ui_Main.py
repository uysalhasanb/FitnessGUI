# Form implementation generated from reading ui file 'c:\Users\Uysalhasanbasri\Documents\FitnessGUI\FitnessGUI\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 20, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 0, 49, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.weighingDateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.weighingDateEdit.setGeometry(QtCore.QRect(10, 170, 110, 22))
        self.weighingDateEdit.setObjectName("weighingDateEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 81, 21))
        self.label.setObjectName("label")
        self.heightSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(10, 230, 62, 22))
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 49, 16))
        self.label_2.setObjectName("label_2")
        self.weightSpinBox_2 = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.weightSpinBox_2.setGeometry(QtCore.QRect(90, 230, 62, 22))
        self.weightSpinBox_2.setObjectName("weightSpinBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 210, 49, 16))
        self.label_3.setObjectName("label_3")
        self.neckSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.neckSpinBox.setGeometry(QtCore.QRect(160, 230, 42, 22))
        self.neckSpinBox.setObjectName("neckSpinBox")
        self.waistSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.waistSpinBox.setGeometry(QtCore.QRect(220, 230, 42, 22))
        self.waistSpinBox.setObjectName("waistSpinBox")
        self.hipSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.hipSpinBox.setGeometry(QtCore.QRect(280, 230, 42, 22))
        self.hipSpinBox.setObjectName("hipSpinBox")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 210, 49, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 210, 49, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 210, 49, 16))
        self.label_5.setObjectName("label_5")
        self.calculatePushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(330, 230, 75, 24))
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.savePushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(420, 230, 75, 24))
        self.savePushButton.setObjectName("savePushButton")
        self.birthDateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.birthDateEdit.setGeometry(QtCore.QRect(290, 20, 110, 22))
        self.birthDateEdit.setObjectName("birthDateEdit")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 0, 81, 21))
        self.label_7.setObjectName("label_7")
        self.genderComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.genderComboBox.setGeometry(QtCore.QRect(420, 20, 121, 22))
        self.genderComboBox.setObjectName("genderComboBox")
        self.bmiLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.bmiLabel.setGeometry(QtCore.QRect(10, 300, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bmiLabel.setFont(font)
        self.bmiLabel.setObjectName("bmiLabel")
        self.fatFiLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fatFiLabel.setGeometry(QtCore.QRect(10, 400, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fatFiLabel.setFont(font)
        self.fatFiLabel.setObjectName("fatFiLabel")
        self.fatUsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fatUsLabel.setGeometry(QtCore.QRect(180, 400, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fatUsLabel.setFont(font)
        self.fatUsLabel.setObjectName("fatUsLabel")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 380, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(180, 380, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 0, 61, 16))
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>syötä tähän oma nimesi</p></body></html>"))
        self.nameLabel.setText(_translate("MainWindow", "Nimi"))
        self.label.setText(_translate("MainWindow", "Mittausspäivä"))
        self.label_2.setText(_translate("MainWindow", "Pituus"))
        self.label_3.setText(_translate("MainWindow", "Paino"))
        self.label_4.setText(_translate("MainWindow", "Lantio"))
        self.label_6.setText(_translate("MainWindow", "Kaula"))
        self.label_5.setText(_translate("MainWindow", "Vyötärö"))
        self.calculatePushButton.setText(_translate("MainWindow", "Laske"))
        self.savePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.label_7.setText(_translate("MainWindow", "Syntymäaika"))
        self.genderComboBox.setPlaceholderText(_translate("MainWindow", "Valitse Sukupuoli"))
        self.bmiLabel.setText(_translate("MainWindow", "Painoindeksi"))
        self.fatFiLabel.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.fatUsLabel.setText(_translate("MainWindow", "Rasvaprosentti (US)"))
        self.label_11.setText(_translate("MainWindow", "Painoindeksi"))
        self.label_12.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.label_13.setText(_translate("MainWindow", "Rasvaprosentti (US)"))
        self.label_14.setText(_translate("MainWindow", "Sukupuoli"))
