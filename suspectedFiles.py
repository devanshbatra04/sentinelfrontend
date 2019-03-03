from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import requests
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.URL = "localhost"
        self.title = "PyQt5 Tables"
        self.top = 100
        self.left = 100
        self.width = 700
        self.height = 400
      #  self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowIcon(QtGui.QIcon("sentinel.png"))
        self.p = 0
        self.n = 0
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.files = requests.post("http://" + self.URL + ":5000/getSuspectFiles").json()['files']
        self.creatingTables()
        VBox = QVBoxLayout()

        VBox.addWidget(self.tableWidget)




        self.setLayout(VBox)

        self.show()

    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.files)-1)
        self.tableWidget.setColumnCount(1)
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setHorizontalHeaderLabels(["Files"])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # self.tableWidget.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))

        # self.tableWidget.setStyleSheet()

        count = 0
        for i in self.files:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(i))
            count = count + 1

    def rerun(self):
         self.creatingTables()

    def suspectedFiles(self):

        import os
        os.system('python ' + 'VTscan.py' + ' ' +  + ' & disown')

        self.files = requests.post("http://" + self.URL + ":5000/getSuspectFiles").json()['files']

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.files))
        self.tableWidget.setColumnCount(1)
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setHorizontalHeaderLabels(["Files"])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


        # self.tableWidget.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))

        # self.tableWidget.setStyleSheet()

        count = 0
        for i in self.files:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(i))
            count = count + 1


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
