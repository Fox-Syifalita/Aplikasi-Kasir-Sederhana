# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1271, 808)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblJudul = QtWidgets.QLabel(self.centralwidget)
        self.lblJudul.setGeometry(QtCore.QRect(240, 160, 741, 151))
        font = QtGui.QFont()
        font.setPointSize(43)
        self.lblJudul.setFont(font)
        self.lblJudul.setObjectName("lblJudul")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 290, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1271, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuData_Barang = QtWidgets.QMenu(self.menubar)
        self.menuData_Barang.setObjectName("menuData_Barang")
        self.menuKasir = QtWidgets.QMenu(self.menubar)
        self.menuKasir.setObjectName("menuKasir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInput_Data_Barang = QtWidgets.QAction(MainWindow)
        self.actionInput_Data_Barang.setObjectName("actionInput_Data_Barang")
        self.actionPoint_Of_Sales = QtWidgets.QAction(MainWindow)
        self.actionPoint_Of_Sales.setObjectName("actionPoint_Of_Sales")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuFile.addAction(self.actionLogout)
        self.menuData_Barang.addAction(self.actionInput_Data_Barang)
        self.menuKasir.addAction(self.actionPoint_Of_Sales)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData_Barang.menuAction())
        self.menubar.addAction(self.menuKasir.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblJudul.setText(_translate("MainWindow", "Warung Makan Bu R"))
        self.label.setText(_translate("MainWindow", "Point of Sales"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuData_Barang.setTitle(_translate("MainWindow", "Data Barang"))
        self.menuKasir.setTitle(_translate("MainWindow", "Kasir"))
        self.actionInput_Data_Barang.setText(_translate("MainWindow", "Input Data Barang"))
        self.actionPoint_Of_Sales.setText(_translate("MainWindow", "Point Of Sales"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

