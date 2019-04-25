# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from user_choice_dialog import Ui_Dialog as dialog
#import user_choice_dialog as uiSelf
import userDatas
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 492)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.idNum = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IDlabel = QtWidgets.QLabel(self.centralwidget)
        self.IDlabel.setGeometry(QtCore.QRect(100, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IDlabel.setFont(font)
        self.IDlabel.setObjectName("IDlabel")
        self.UserId = QtWidgets.QLabel(self.centralwidget)
        self.UserId.setGeometry(QtCore.QRect(160, 70, 91, 31))
        self.UserId.setFont(font)
        self.UserId.setObjectName("UserId")
        self.UserId.setText("ID'yi tuşla")
        #self.IDinput = QtWidgets.QLineEdit(self.centralwidget)
        #self.IDinput.setGeometry(QtCore.QRect(160, 70, 91, 31))
        #self.IDinput.setObjectName("IDinput")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(270, 70, 81, 31))
        #self.enterButton.clicked.connect(self.setUser)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton.setFont(font)
        self.enterButton.setObjectName("enterButton")
        self.enterButton.clicked.connect(self.enterButton_clicked)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 110, 111, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.KeyPad = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.KeyPad.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.KeyPad.setContentsMargins(0, 0, 0, 0)
        self.KeyPad.setObjectName("KeyPad")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.num0 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num0.setFont(font)
        self.num0.setObjectName("num0")
        self.num0.clicked.connect(self.num0_clicked)
        self.verticalLayout.addWidget(self.num0)
        self.num2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num2.setFont(font)
        self.num2.setObjectName("num2")
        self.num2.clicked.connect(self.num2_clicked)
        self.verticalLayout.addWidget(self.num2)
        self.num4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num4.setFont(font)
        self.num4.setObjectName("num4")
        self.num4.clicked.connect(self.num4_clicked)
        self.verticalLayout.addWidget(self.num4)
        self.num6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num6.setFont(font)
        self.num6.setObjectName("num6")
        self.num6.clicked.connect(self.num6_clicked)
        self.verticalLayout.addWidget(self.num6)
        self.num8 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num8.setFont(font)
        self.num8.setObjectName("num8")
        self.num8.clicked.connect(self.num8_clicked)
        self.verticalLayout.addWidget(self.num8)
        self.KeyPad.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.num1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.num1.clicked.connect(self.num1_clicked)
        self.verticalLayout_2.addWidget(self.num1)
        self.num3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num3.setFont(font)
        self.num3.setObjectName("num3")
        self.num3.clicked.connect(self.num3_clicked)
        self.verticalLayout_2.addWidget(self.num3)
        self.num5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num5.setFont(font)
        self.num5.setObjectName("num5")
        self.num5.clicked.connect(self.num5_clicked)
        self.verticalLayout_2.addWidget(self.num5)
        self.num7 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num7.setFont(font)
        self.num7.setObjectName("num7")
        self.num7.clicked.connect(self.num7_clicked)
        self.verticalLayout_2.addWidget(self.num7)
        self.num9 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.num9.setFont(font)
        self.num9.setObjectName("num9")
        self.num9.clicked.connect(self.num9_clicked)
        self.verticalLayout_2.addWidget(self.num9)
        self.KeyPad.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 20, 271, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.greetingHeader = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.greetingHeader.setObjectName("greetingHeader")
        self.verticalLayout_3.addWidget(self.greetingHeader)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit_FullScreen = QtWidgets.QAction(MainWindow)
        self.actionExit_FullScreen.setObjectName("actionExit_FullScreen")
        self.menuFile.addAction(self.actionExit_FullScreen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit_FullScreen.triggered.connect(MainWindow.showNormal)
        #self.enterButton.clicked['bool'].connect(self.IDinput.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def num0_clicked(self):
        if len(self.idNum) <= 4: 
            self.idNum += "0"
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
        #self.UserId.setText(self.idNum)
    def num1_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "1" #self.idNum.join("1")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num2_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "2" # self.idNum.join("2")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num3_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum +=  "3" #self.idNum.join("3")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num4_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "4" #self.idNum.join("4")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num5_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "5" #self.idNum.join("5")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num6_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "6" #self.idNum.join("6")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num7_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "7" #self.idNum.join("7")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num8_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "8" #self.idNum.join("8")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def num9_clicked(self):
        if len(self.idNum) < 4: 
            self.idNum += "9" #self.idNum.join("9")
            self.UserId.setText(self.idNum)
        else:
            self.UserId.setText("Yanlış ID")
            self.idNum = ""
    def enterButton_clicked(self):
        if self.idNum in userDatas.usersDict["UserData"]:
            data = userDatas.usersDict["UserData"][self.idNum]
            print(data["User Name"])
            Dialog = QtWidgets.QDialog()
            ui = dialog()
            ui.idNum = self.idNum
            ui.setupUi(Dialog)
            ui.label.setText("Merhaba {}".format(data["User Name"]))
            Dialog.showFullScreen()
            Dialog.exec_()
        else:
            self.UserId.setText("Yanlış ID")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mekatroniğin Esasları"))
        self.IDlabel.setText(_translate("MainWindow", "ID: "))
        self.enterButton.setText(_translate("MainWindow", "Giriş"))
        self.num0.setText(_translate("MainWindow", "0"))
        self.num2.setText(_translate("MainWindow", "2"))
        self.num4.setText(_translate("MainWindow", "4"))
        self.num6.setText(_translate("MainWindow", "6"))
        self.num8.setText(_translate("MainWindow", "8"))
        self.num1.setText(_translate("MainWindow", "1"))
        self.num3.setText(_translate("MainWindow", "3"))
        self.num5.setText(_translate("MainWindow", "5"))
        self.num7.setText(_translate("MainWindow", "7"))
        self.num9.setText(_translate("MainWindow", "9"))
        self.greetingHeader.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">SportRonix\'e Hoş Geldiniz</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit_FullScreen.setText(_translate("MainWindow", "Exit FullScreen"))
        self.actionExit_FullScreen.setStatusTip(_translate("MainWindow", "Click to Exit Fullscreen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())

