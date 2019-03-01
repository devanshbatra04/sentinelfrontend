# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickScanResult.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
URL = "localhost:5000"

class quickScanWindow(object):
    def setupUi(self, MainWindow, data):
        response = requests.post(url='http://%s/getReport' % URL, data={"filepath": data})
        json_response = response.json()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 361, 61))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 121, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("sentinel.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 120, 531, 281))
        self.frame.setStyleSheet("QLabel { color : green; }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.MessageLabel = QtWidgets.QLabel(self.frame)
        self.MessageLabel.setGeometry(QtCore.QRect(60, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.MessageLabel.setFont(font)
        self.MessageLabel.setMouseTracking(False)
        self.MessageLabel.setStyleSheet("QLabel { color : green; }")
        self.MessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MessageLabel.setObjectName("MessageLabel")
        self.FileLabel = QtWidgets.QLabel(self.frame)
        self.FileLabel.setGeometry(QtCore.QRect(110, 50, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.FileLabel.setFont(font)
        self.FileLabel.setMouseTracking(False)
        self.FileLabel.setStyleSheet("QLabel { color : rgb(171, 24, 82); }")
        self.FileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FileLabel.setObjectName("FileLabel")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(360, 100, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 180, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel { font-weight: 600; color : rgb(0, 0, 0); }")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel { font-weight: 600; color : rgb(0, 0, 0); }")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel { font-weight: 600; color : rgb(0, 0, 0); }")
        self.label_7.setObjectName("label_7")
        self.ScanTime = QtWidgets.QLabel(self.frame)
        self.ScanTime.setGeometry(QtCore.QRect(150, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.ScanTime.setFont(font)
        self.ScanTime.setMouseTracking(False)
        self.ScanTime.setStyleSheet("QLabel { color : rgb(171, 24, 82); }")
        self.ScanTime.setAlignment(QtCore.Qt.AlignCenter)
        self.ScanTime.setObjectName("ScanTime")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(140, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(False)
        self.label_9.setStyleSheet("QLabel { color : blue; }")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.PositiveVal = QtWidgets.QLabel(self.frame)
        self.PositiveVal.setGeometry(QtCore.QRect(140, 160, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PositiveVal.setFont(font)
        self.PositiveVal.setMouseTracking(False)
        self.PositiveVal.setStyleSheet("QLabel { font-weight:600;  color : rgb(239, 41, 41); }")
        self.PositiveVal.setAlignment(QtCore.Qt.AlignCenter)
        self.PositiveVal.setObjectName("PositiveVal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, json_response)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow, json_response):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "File Scan Results"))
        self.MessageLabel.setText(_translate("MainWindow", json_response.get("message")))
        self.FileLabel.setText(_translate("MainWindow", json_response.get("file")))
        self.pushButton.setText(_translate("MainWindow", "Delete File"))
        self.pushButton_2.setText(_translate("MainWindow", "Get Process Details"))
        self.label_5.setText(_translate("MainWindow", "Total Scans"))
        self.label_6.setText(_translate("MainWindow", "Positives"))
        self.label_7.setText(_translate("MainWindow", "Scan Time"))
        self.ScanTime.setText(_translate("MainWindow", json_response.get("scan date")))
        self.label_9.setText(_translate("MainWindow", str(json_response.get("total scans"))))
        self.PositiveVal.setText(_translate("MainWindow", str(json_response.get("positives"))))


import sys
app = QtWidgets.QApplication(['quickScanResult.py'])
MainWindow = QtWidgets.QMainWindow()
ui = quickScanWindow()
# ui.setupUi(MainWindow)
ui.setupUi(MainWindow, sys.argv[1])
MainWindow.show()
sys.exit(app.exec_())

