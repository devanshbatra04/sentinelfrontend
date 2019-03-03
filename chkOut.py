# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'malwarescans.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 445)
        self.URL = "localhost"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(120, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sentinel.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.HLine)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(239, 41, 41);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.positive = QtWidgets.QLabel(self.centralwidget)
        self.positive.setObjectName("positive")
        self.horizontalLayout_8.addWidget(self.positive)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("color: rgb(32, 74, 135);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.negative = QtWidgets.QLabel(self.centralwidget)
        self.negative.setObjectName("negative")
        self.horizontalLayout_9.addWidget(self.negative)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.get_files = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_files.sizePolicy().hasHeightForWidth())
        self.get_files.setSizePolicy(sizePolicy)
        self.get_files.setMinimumSize(QtCore.QSize(143, 0))
        self.get_files.setObjectName("get_files")
        self.verticalLayout_7.addWidget(self.get_files)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.output = {}
        self.results = []
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Sentinel - CHKROOKIT Administration"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Rootkit Signature"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Result"))
        self.label_3.setText(_translate("MainWindow", "Positives:"))
        self.positive.setText(_translate("MainWindow", "23"))
        self.label_4.setText(_translate("MainWindow", "Negatives:"))
        self.negative.setText(_translate("MainWindow", "44"))
        self.get_files.setText(_translate("MainWindow", "Rerun Scan"))
        self.pushButton_2.setText(_translate("MainWindow", "GetFilesOnly"))
        self.output = requests.post("http://" + self.URL + ":5000/getchkrScanResults").json()

        print(self.output)
        self.results = self.output["results"]
        print(self.results)
    #     self.creatingTables()
    #
    # def creatingTables(self):
    #     self.tableWidget = QTableWidget(self.centralwidget)
    #     self.tableWidget.setEnabled(True)
    #     self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1290, 400))
    #     self.tableWidget.setRowCount(len(self.results))
    #     self.tableWidget.setColumnCount(2)
    #
    #     header = self.tableWidget.horizontalHeader()
    #     self.tableWidget.setHorizontalHeaderLabels(["RootKit Signature", "Scan Result"])
    #     header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    #     header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    #
    #
    #     count = 0
    #     for item in self.results:
    #         print(item)
    #         print(count)
    #         self.tableWidget.setItem(count, 0, QTableWidgetItem(item['infection_name']))
    #         self.tableWidget.setItem(count, 1, QTableWidgetItem(str(item['scan_result'])))
    #
    #         count = count + 1
    #
    #     self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
    #
    #     self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
