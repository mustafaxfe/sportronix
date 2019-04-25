# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Day3Program.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
#from day1prog import Ui_Form as day1q
import day2prog, day1prog 
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 329)
        self.idNum = "1010"
        self.omuzDict = json.load(open("omuz.txt"))
        self.bicepsDict = json.load(open("biceps.txt"))
        self.bacakDict = json.load(open("bacak.txt"))
        self.gogusDict = json.load(open("gogus.txt"))
        self.triceptDict = json.load(open("tricept.txt"))
        self.torbaDict = json.load(open("torba.txt"))
        self.sirtDict = json.load(open("sırt.txt"))
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 321, 291))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 305, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 371, 341))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 281, 221))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.Kosu = QtWidgets.QWidget()
        self.Kosu.setObjectName("Kosu")
        self.label = QtWidgets.QLabel(self.Kosu)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 191))
        #self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("../../../.designer/backup/koşu.png"))
        #self.label.setObjectName("label")
        #self.textBrowser = QtWidgets.QTextBrowser(self.Kosu)
        #self.textBrowser.setGeometry(QtCore.QRect(260, 10, 121, 192))
        #self.textBrowser.setSearchPaths(['Saat', '', 'aaa'])
        #self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(self.Kosu)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 171, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("koşu.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Kosu)
        self.label_7.setGeometry(QtCore.QRect(180, 20, 71, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.Kosu, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, -10, 251, 171))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(-30, 10, 251, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("milPress.jpg"))
        self.label_2.setObjectName("label_2")
        self.milPress = QtWidgets.QLabel(self.tab_3)
        self.milPress.setGeometry(QtCore.QRect(20, 120, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.milPress.setFont(font)
        self.milPress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.milPress.setAutoFillBackground(False)
        self.milPress.setObjectName("milPress")
        self.tabWidget_2.addTab(self.tab_3, "Military Press")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(90, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.milPress_2 = QtWidgets.QLabel(self.tab_5)
        self.milPress_2.setGeometry(QtCore.QRect(220, 160, 81, 31))
        self.milPress_2.setText("")
        self.milPress_2.setObjectName("milPress_2")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("litRaise.jpg"))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam Unjoined")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.overPressSet_2 = QtWidgets.QLabel(self.tab_6)
        self.overPressSet_2.setGeometry(QtCore.QRect(210, 170, 54, 17))
        self.overPressSet_2.setObjectName("overPressSet_2")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(-10, 20, 231, 81))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("overPress.jpg"))
        self.label_9.setObjectName("label_9")
        self.overPress = QtWidgets.QLabel(self.tab_6)
        self.overPress.setGeometry(QtCore.QRect(10, 110, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam Unjoined")
        font.setPointSize(14)
        self.overPress.setFont(font)
        self.overPress.setObjectName("overPress")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 171, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("seaDumbell.jpg"))
        self.label_3.setObjectName("label_3")
        self.seatPress = QtWidgets.QLabel(self.tab_4)
        self.seatPress.setGeometry(QtCore.QRect(10, 130, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam Unjoined")
        font.setPointSize(14)
        self.seatPress.setFont(font)
        self.seatPress.setObjectName("seatPress")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 271, 151))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(10)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_12 = QtWidgets.QLabel(self.tab_7)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 211, 91))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("hammer_curl.jpeg"))
        self.label_12.setObjectName("label_12")
        self.hamCurl = QtWidgets.QLabel(self.tab_7)
        self.hamCurl.setGeometry(QtCore.QRect(10, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam Unjoined")
        font.setPointSize(14)
        self.hamCurl.setFont(font)
        self.hamCurl.setObjectName("hamCurl")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_11 = QtWidgets.QLabel(self.tab_8)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 211, 81))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("babCurl.jpg"))
        self.label_11.setObjectName("label_11")
        self.babDumbell = QtWidgets.QLabel(self.tab_8)
        self.babDumbell.setGeometry(QtCore.QRect(10, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam Unjoined")
        font.setPointSize(14)
        self.babDumbell.setFont(font)
        self.babDumbell.setObjectName("babDumbell")
        self.tabWidget_3.addTab(self.tab_8, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 231, 91))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("incline_dumbell.jpeg"))
        self.label_10.setObjectName("label_10")
        self.incDumbel = QtWidgets.QLabel(self.widget)
        self.incDumbel.setGeometry(QtCore.QRect(10, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam Unjoined")
        font.setPointSize(14)
        self.incDumbel.setFont(font)
        self.incDumbel.setObjectName("incDumbel")
        self.tabWidget_3.addTab(self.widget, "")
        self.tabWidget.addTab(self.tab, "")
        self.bacak = QtWidgets.QWidget()
        self.bacak.setObjectName("bacak")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.bacak)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 271, 161))
        self.tabWidget_4.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.squat = QtWidgets.QWidget()
        self.squat.setObjectName("squat")
        self.label_13 = QtWidgets.QLabel(self.squat)
        self.label_13.setGeometry(QtCore.QRect(30, 10, 141, 81))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("squat.png"))
        self.label_13.setObjectName("label_13")
        self.squat_label = QtWidgets.QLabel(self.squat)
        self.squat_label.setGeometry(QtCore.QRect(20, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setItalic(True)
        self.squat_label.setFont(font)
        self.squat_label.setObjectName("squat_label")
        self.tabWidget_4.addTab(self.squat, "")
        self.labEx = QtWidgets.QWidget()
        self.labEx.setObjectName("labEx")
        self.labExe = QtWidgets.QLabel(self.labEx)
        self.labExe.setGeometry(QtCore.QRect(10, 40, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labExe.setFont(font)
        self.labExe.setObjectName("labExe")
        self.tabWidget_4.addTab(self.labEx, "")
        self.tabWidget.addTab(self.bacak, "")
        self.gogus = QtWidgets.QWidget()
        self.gogus.setObjectName("gogus")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.gogus)
        self.tabWidget_5.setGeometry(QtCore.QRect(10, 0, 261, 151))
        self.tabWidget_5.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.bench = QtWidgets.QWidget()
        self.bench.setObjectName("bench")
        self.label_14 = QtWidgets.QLabel(self.bench)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 141, 81))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("bench.png"))
        self.label_14.setObjectName("label_14")
        self.bench_2 = QtWidgets.QLabel(self.bench)
        self.bench_2.setGeometry(QtCore.QRect(10, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        self.bench_2.setFont(font)
        self.bench_2.setObjectName("bench_2")
        self.tabWidget_5.addTab(self.bench, "")
        self.cableC = QtWidgets.QWidget()
        self.cableC.setObjectName("cableC")
        self.label_15 = QtWidgets.QLabel(self.cableC)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 161, 101))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("cablecross.png"))
        self.label_15.setObjectName("label_15")
        self.cableCro = QtWidgets.QLabel(self.cableC)
        self.cableCro.setGeometry(QtCore.QRect(10, 110, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(14)
        font.setItalic(True)
        self.cableCro.setFont(font)
        self.cableCro.setObjectName("cableCro")
        self.tabWidget_5.addTab(self.cableC, "")
        self.dumbell = QtWidgets.QWidget()
        self.dumbell.setObjectName("dumbell")
        self.label_16 = QtWidgets.QLabel(self.dumbell)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 161, 81))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("dumbellFly.png"))
        self.label_16.setObjectName("label_16")
        self.dumbellFlu = QtWidgets.QLabel(self.dumbell)
        self.dumbellFlu.setGeometry(QtCore.QRect(10, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dumbellFlu.setFont(font)
        self.dumbellFlu.setObjectName("dumbellFlu")
        self.tabWidget_5.addTab(self.dumbell, "")
        self.tabWidget.addTab(self.gogus, "")
        self.triceps = QtWidgets.QWidget()
        self.triceps.setObjectName("triceps")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.triceps)
        self.tabWidget_6.setGeometry(QtCore.QRect(10, 10, 251, 141))
        self.tabWidget_6.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.Dips = QtWidgets.QWidget()
        self.Dips.setObjectName("Dips")
        self.label_17 = QtWidgets.QLabel(self.Dips)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 161, 81))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("dips.png"))
        self.label_17.setObjectName("label_17")
        self.dips = QtWidgets.QLabel(self.Dips)
        self.dips.setGeometry(QtCore.QRect(10, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dips.setFont(font)
        self.dips.setTextFormat(QtCore.Qt.PlainText)
        self.dips.setObjectName("dips")
        self.tabWidget_6.addTab(self.Dips, "")
        self.crosshers = QtWidgets.QWidget()
        self.crosshers.setObjectName("crosshers")
        self.label_18 = QtWidgets.QLabel(self.crosshers)
        self.label_18.setGeometry(QtCore.QRect(20, 10, 161, 81))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("skull.png"))
        self.label_18.setObjectName("label_18")
        self.skull = QtWidgets.QLabel(self.crosshers)
        self.skull.setGeometry(QtCore.QRect(20, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.skull.setFont(font)
        self.skull.setObjectName("skull")
        self.tabWidget_6.addTab(self.crosshers, "")
        self.tabWidget.addTab(self.triceps, "")
        self.sirt = QtWidgets.QWidget()
        self.sirt.setObjectName("sirt")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.sirt)
        self.tabWidget_7.setGeometry(QtCore.QRect(10, 10, 251, 141))
        self.tabWidget_7.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.Barfiks = QtWidgets.QWidget()
        self.Barfiks.setObjectName("Barfiks")
        self.label_20 = QtWidgets.QLabel(self.Barfiks)
        self.label_20.setGeometry(QtCore.QRect(20, 10, 151, 91))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("barfiks.png"))
        self.label_20.setObjectName("label_20")
        self.Barfiks_2 = QtWidgets.QLabel(self.Barfiks)
        self.Barfiks_2.setGeometry(QtCore.QRect(50, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Barfiks_2.setFont(font)
        self.Barfiks_2.setObjectName("Barfiks_2")
        self.tabWidget_7.addTab(self.Barfiks, "")
        self.deadlift = QtWidgets.QWidget()
        self.deadlift.setObjectName("deadlift")
        self.label_21 = QtWidgets.QLabel(self.deadlift)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 161, 81))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("dead.png"))
        self.label_21.setObjectName("label_21")
        self.dead = QtWidgets.QLabel(self.deadlift)
        self.dead.setGeometry(QtCore.QRect(20, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dead.setFont(font)
        self.dead.setTextFormat(QtCore.Qt.PlainText)
        self.dead.setObjectName("dead")
        self.tabWidget_7.addTab(self.deadlift, "")
        self.tbar = QtWidgets.QWidget()
        self.tbar.setObjectName("tbar")
        self.label_22 = QtWidgets.QLabel(self.tbar)
        self.label_22.setGeometry(QtCore.QRect(20, 10, 141, 81))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("tbar.png"))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tbar)
        self.label_23.setGeometry(QtCore.QRect(10, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.tabWidget_7.addTab(self.tbar, "")
        self.tabWidget.addTab(self.sirt, "")
        self.torba = QtWidgets.QWidget()
        self.torba.setObjectName("torba")
        self.label_19 = QtWidgets.QLabel(self.torba)
        self.label_19.setGeometry(QtCore.QRect(50, 0, 161, 111))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("torba.png"))
        self.label_19.setObjectName("label_19")
        self.torba_2 = QtWidgets.QLabel(self.torba)
        self.torba_2.setGeometry(QtCore.QRect(40, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.torba_2.setFont(font)
        self.torba_2.setObjectName("torba_2")
        self.tabWidget.addTab(self.torba, "")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 20, 137, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Close)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.day1_clicked)
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.day2_clicked)
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_2.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(1)
        self.tabWidget_7.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def day1_clicked(self):
        app = QtWidgets.QWidget()
        ui = day1prog.Ui_Form()
        ui.setupUi(app)
        app.show()
        app.exec_()
    def day2_clicked(self):
        app = QtWidgets.QWidget()
        ui = day2prog.Ui_Form()
        ui.setupUi(app)
        app.show()
        app.exec_()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "3. Günün Programı"))
        self.tabWidget.setToolTip(_translate("Form", "<html><head/><body><p>Koşu</p></body></html>"))
        if "Day3" in self.omuzDict[self.idNum]:
            self.milPress.setText("Set/Tekrar" + self.omuzDict[self.idNum]["Day3"]["Military Press"])
            self.label_4.setText("Set/Tekrar" + self.omuzDict[self.idNum]["Day3"]["Literal Press"])
            self.overPress.setText("Set/Tekrar" + self.omuzDict[self.idNum]["Day3"]["Overhead Press"])
            self.seatPress.setText("Set/Tekrar" + self.omuzDict[self.idNum]["Day3"]["Seated Dumbell Press"])
            
        else:
            print("hımm")
            self.milPress.setText("Bugun Yok")
            self.label_4.setText("Bugün Yok")
            self.overPress.setText("Bugün Yok")
            self.seatPress.setText("Bugün Yok")
        if "Day3" in self.bicepsDict[self.idNum]:
            self.hamCurl.setText("Set/Tekrar" + self.bicepsDict[self.idNum]["Day3"]["Hammer Curl"])
            self.babDumbell.setText("Set/Tekrar" + self.bicepsDict[self.idNum]["Day3"]["Babell Curl"])
            self.incDumbel.setText("Set/Tekrar" + self.bicepsDict[self.idNum]["Day3"]["Incline Dumbell"])
        else:
            self.hamCurl.setText("Bugun Yok")
            self.babDumbell.setText("Bugun Yok")
            self.incDumbel.setText("Bugun Yok")
        if "Day3" in self.bacakDict[self.idNum]:
            self.squat_label.setText("Set/Tekrar" + self.bacakDict[self.idNum]["Day3"]["Squat"])
            self.labExe.setText("Set/Tekrar" + self.bacakDict[self.idNum]["Day3"]["Lab execution"])
        else:
            self.squat_label.setText("Bugun Yok")
            self.labExe.setText("Bugun Yok")
        if "Day3" in self.gogusDict[self.idNum]:
            self.bench_2.setText("Set/Tekrar" + self.gogusDict[self.idNum]["Day3"]["Bench Press"])
            self.cableCro.setText("Set/Tekrar" + self.gogusDict[self.idNum]["Day3"]["Cable Cross"])
            self.dumbellFlu.setText("Set/Tekrar" + self.gogusDict[self.idNum]["Day3"]["Dumbell Cross"])
        else:
            self.bench_2.setText("Bugun Yok")
            self.cableCro.setText("Bugun Yok")
            self.dumbellFlu.setText("Bugun Yok")
        if "Day3" in self.triceptDict[self.idNum]:
            self.dips.setText("Set/Tekrar" + self.triceptDict[self.idNum]["Day3"]["Dips"])
            self.skull.setText("Set/Tekrar" + self.triceptDict[self.idNum]["Day3"]["Skull Crossers"])
        else:
            self.dips.setText("Bugun Yok")
            self.skull.setText("Bugun Yok")
        if "Day3" in self.torbaDict[self.idNum]:
            self.torba_2.setText(_translate("Form", "2li 3lü yumruklar"))
        else:
            self.torba_2.setText("Bugün Yok")
        if "Day3" in self.sirtDict[self.idNum]:
            self.Barfiks_2.setText("Set/Tekrar" + self.triceptDict[self.idNum]["Day3"]["Barfiks"])
            self.dead.setText("Set/Tekrar" + self.triceptDict[self.idNum]["Day3"]["Dead Lift"])
            self.label_23.setText("Set/Tekrar" + self.triceptDict[self.idNum]["Day3"]["T Bar Row"])

        else:
            self.Barfiks_2.setText("Bugün Yok")
            self.dead.setText("Bugün Yok")
            self.label_23.setText("Bugün Yok")
        self.label_7.setText(_translate("Form", "30 Dk"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Kosu), _translate("Form", "Koşu"))
        #self.milPress.setText(_translate("Form", "Set/Tekrar: 3x10"))
        #self.label_5.setText(_translate("Form", "Set / Tekrar"))
        #self.label_4.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "Literal Rise"))
        self.overPressSet_2.setText(_translate("Form", "TextLabel"))
        #self.overPress.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "Overhead Press"))
        #self.seatPress.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Seated Dumbel Press"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Omuz"))
        #self.hamCurl.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("Form", "Hammer Curl"))
        #self.babDumbell.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("Form", "Babell Curl"))
        #self.incDumbel.setText(_translate("Form", "Set/Tekrar: 4x10"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.widget), _translate("Form", "Inurlcline Dumbel C"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Biceps"))
        #self.squat_label.setText(_translate("Form", "Set/Tekrar: 5x15"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.squat), _translate("Form", "SQUAT"))
        #self.labExe.setText(_translate("Form", "Set/Tekrar: 5x15"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.labEx), _translate("Form", "Lap Exe"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bacak), _translate("Form", "Bacak"))
        #self.bench_2.setText(_translate("Form", "Set/Tekrar: 5x15"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.bench), _translate("Form", "Bench Press"))
        #self.cableCro.setText(_translate("Form", "Set/Tekrar: 5x15"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.cableC), _translate("Form", "Cable Cross"))
        #self.dumbellFlu.setText(_translate("Form", "Set/Tekrar: 3x15"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.dumbell), _translate("Form", "Dumbell FLy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gogus), _translate("Form", "Göğüs"))
        #self.dips.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.Dips), _translate("Form", "Dips"))
        #self.skull.setText(_translate("Form", "Set/Tekrar: 3x10"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.crosshers), _translate("Form", "Crosshers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.triceps), _translate("Form", "Triceps"))
        #self.Barfiks_2.setText(_translate("Form", "Sayı Yok"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Barfiks), _translate("Form", "Barfiks"))
        #self.dead.setText(_translate("Form", "Set/Tekrar: 5x10"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.deadlift), _translate("Form", "DeadLift"))
        #self.label_23.setText(_translate("Form", "Set/Tekrar: 5x10"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tbar), _translate("Form", "TBar Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sirt), _translate("Form", "Sırt"))
        #self.torba_2.setText(_translate("Form", "2li 3lü yumruklar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.torba), _translate("Form", "Torba"))
        self.pushButton.setText(_translate("Form", "Geri"))
        self.pushButton_2.setText(_translate("Form", "1. Gün"))
        self.pushButton_3.setText(_translate("Form", "2. Gün"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showFullScreen()
    sys.exit(app.exec_())