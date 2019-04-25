# -*- coding: utf-8 -*-ImportError: cannot import name 'Ui_MainWindow'

# Form implementation generated from reading ui file 'dialog_user_choice3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import measure_dialog #import Ui_Dialog as measurement
import dailyDialog #import Ui_Dialog as programSchedule
#import MainWin
#from MainWin import Ui_MainWindow as mainWin
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.idNum = ""
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Olculer = QtWidgets.QPushButton(Dialog)
        self.Olculer.setGeometry(QtCore.QRect(60, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Olculer.setFont(font)
        self.Olculer.setObjectName("Olculer")
        self.Olculer.clicked.connect(self.olculer_clicked)
        self.Program = QtWidgets.QPushButton(Dialog)
        self.Program.setGeometry(QtCore.QRect(210, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Program.setFont(font)
        self.Program.setObjectName("Program")
        self.Program.clicked.connect(self.program_clicked)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def program_clicked(self):
        Dialog = QtWidgets.QDialog()
        #Dialog.close()
        ui = dailyDialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.showFullScreen()
        sys.exit(Dialog.exec_())
    def Close(self):
        Dialog = QtWidgets.QtDialog()
        Dialog.close()
        import os
        os.system("python3 MainWin.py")
        #import sys

    def olculer_clicked(self):
        #global Form
        import sys
        global app
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = measure_dialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.showFullScreen()
        sys.exit(Dialog.exec_())
        #Form.exec_()
        #sys.exit(Form.exec_())
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Olculer.setText(_translate("Dialog", "Ölçüler"))
        self.Program.setText(_translate("Dialog", "Program"))
        self.pushButton.setText(_translate("Dialog", "Geri"))
        self.label.setText(_translate("Dialog", "Merhaba Mustafa"))


if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.showFullScreen()
    sys.exit(app.exec_())

