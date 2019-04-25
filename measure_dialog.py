# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measure_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import userDatas
import json
import user_choice_dialog, sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 446)
        self.idNum = "1010"
        self.userDicts = json.load(open("usersValues.txt"))

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 10, 221, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tricepsLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.tricepsLabel.setFont(font)
        self.tricepsLabel.setObjectName("tricepsLabel")
        self.verticalLayout_4.addWidget(self.tricepsLabel)
        self.belLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.belLabel.setFont(font)
        self.belLabel.setObjectName("belLabel")
        self.verticalLayout_4.addWidget(self.belLabel)
        self.bacakLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bacakLabel.setFont(font)
        self.bacakLabel.setObjectName("bacakLabel")
        self.verticalLayout_4.addWidget(self.bacakLabel)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.intSpinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.intSpinBox_2.setFont(font)
        self.intSpinBox_2.setObjectName("intSpinBox_2")
        self.intSpinBox_2.setValue(self.userDicts["UserData"][self.idNum]["Triceps"])
        self.intSpinBox_2.setMaximum(200)
        self.intSpinBox_2.valueChanged.connect(self.valueChanged_2)

        self.verticalLayout_5.addWidget(self.intSpinBox_2)
        self.intSpinBox_7 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.intSpinBox_7.setFont(font)
        self.intSpinBox_7.setObjectName("intSpinBox_7")
        self.intSpinBox_7.setValue(self.userDicts["UserData"][self.idNum]["Bel"])
        self.intSpinBox_7.setMaximum(200)
        self.intSpinBox_7.valueChanged.connect(self.valueChanged_7)
        self.verticalLayout_5.addWidget(self.intSpinBox_7)
        self.intSpinBox_8 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.intSpinBox_8.setFont(font)
        self.intSpinBox_8.setObjectName("intSpinBox_8")
        self.intSpinBox_8.setValue(self.userDicts["UserData"][self.idNum]["Bacak"])
        self.intSpinBox_8.setMaximum(200)
        self.intSpinBox_8.valueChanged.connect(self.valueChanged_8)
        self.verticalLayout_5.addWidget(self.intSpinBox_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(140, 160, 301, 61))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Close)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.saveValues)
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1, 10, 220, 151))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.boyLabel = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.boyLabel.setFont(font)
        self.boyLabel.setObjectName("boyLabel")
        self.verticalLayout_2.addWidget(self.boyLabel)
        self.KiloLabel = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.KiloLabel.setFont(font)
        self.KiloLabel.setObjectName("KiloLabel")
        self.verticalLayout_2.addWidget(self.KiloLabel)
        self.bicepsLabel = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bicepsLabel.setFont(font)
        self.bicepsLabel.setObjectName("bicepsLabel")
        self.verticalLayout_2.addWidget(self.bicepsLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.intSpinBox_5 = QtWidgets.QSpinBox(self.layoutWidget_3)
        self.intSpinBox_5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.intSpinBox_5.setFont(font)
        self.intSpinBox_5.setObjectName("intSpinBox_5")
        self.intSpinBox_5.setValue(self.userDicts["UserData"][self.idNum]["Boy"])
        self.intSpinBox_5.valueChanged.connect(self.valueChanged_5)
        self.intSpinBox_5.setMaximum(200)
        self.verticalLayout_3.addWidget(self.intSpinBox_5)
        self.intSpinBox_6 = QtWidgets.QSpinBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.intSpinBox_6.setFont(font)
        self.intSpinBox_6.setObjectName("intSpinBox_6")
        self.intSpinBox_6.setMaximum(200)
        self.intSpinBox_6.valueChanged.connect(self.valueChanged_6)
        self.intSpinBox_6.setValue(self.userDicts["UserData"][self.idNum]["Kilo"])
        self.verticalLayout_3.addWidget(self.intSpinBox_6)
        self.intSpinBox_4 = QtWidgets.QSpinBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.intSpinBox_4.setFont(font)
        self.intSpinBox_4.setObjectName("intSpinBox_4")
        self.intSpinBox_4.setValue(self.userDicts["UserData"][self.idNum]["Biceps"])
        self.intSpinBox_4.setMaximum(200)
        self.intSpinBox_4.valueChanged.connect(self.valueChanged_4)

        self.verticalLayout_3.addWidget(self.intSpinBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tricepsLabel.setBuddy(self.intSpinBox_2)
        self.belLabel.setBuddy(self.intSpinBox_7)
        self.bacakLabel.setBuddy(self.intSpinBox_8)
        self.boyLabel.setBuddy(self.intSpinBox_5)
        self.KiloLabel.setBuddy(self.intSpinBox_6)
        self.bicepsLabel.setBuddy(self.intSpinBox_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def Close(self):
        Dialog = QtWidgets.QDialog()
        Dialog.close()
        ui = user_choice_dialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.showFullScreen()
        sys.exit(Dialog.exec_())        #app.close()
    def saveValues(self):
        json.dump(self.userDicts, open("usersValues.txt",'w'))
     #   f = open("UserDatas.py", "r"):
      #      for item in f.usersDict:
       #         print(item)
    def valueChanged_2(self):
        print(self.intSpinBox_2.value())
        #newDict = userDatas.usersDict
        #newDict["UserData"]["1010"]
        self.userDicts["UserData"][self.idNum]["Triceps"] = self.intSpinBox_2.value()
    def valueChanged_5(self):
        self.userDicts["UserData"][self.idNum]["Boy"] = self.intSpinBox_5.value()
    def valueChanged_6(self):
        self.userDicts["UserData"][self.idNum]["Kilo"] = self.intSpinBox_6.value() 
    def valueChanged_4(self):
        self.userDicts["UserData"][self.idNum]["Biceps"] = self.intSpinBox_4.value()
    def valueChanged_7(self):
        self.userDicts["UserData"][self.idNum]["Bel"] = self.intSpinBox_7.value()
    def valueChanged_8(self):
        self.userDicts["UserData"][self.idNum]["Bacak"] = self.intSpinBox_8.value()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tricepsLabel.setText(_translate("Dialog", "Triceps:"))
        self.belLabel.setText(_translate("Dialog", "Bel:"))
        self.bacakLabel.setText(_translate("Dialog", "Bacak: "))
        self.pushButton_2.setText(_translate("Dialog", "Geri"))
        self.pushButton.setText(_translate("Dialog", "Kaydet"))
        self.boyLabel.setText(_translate("Dialog", "Boy:"))
        self.KiloLabel.setText(_translate("Dialog", "Kilo:"))
        self.bicepsLabel.setText(_translate("Dialog", "Biceps: "))

if __name__ == "__main__":
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.showFullScreen()
    sys.exit(app.exec_())