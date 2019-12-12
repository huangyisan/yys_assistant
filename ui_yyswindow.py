# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yyswindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(265, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.first_page = QtWidgets.QWidget()
        self.first_page.setObjectName("first_page")
        self.gridLayout = QtWidgets.QGridLayout(self.first_page)
        self.gridLayout.setObjectName("gridLayout")
        self.resolution_label = QtWidgets.QLabel(self.first_page)
        self.resolution_label.setObjectName("resolution_label")
        self.gridLayout.addWidget(self.resolution_label, 0, 0, 1, 1)
        self.btn_resolution = QtWidgets.QPushButton(self.first_page)
        self.btn_resolution.setObjectName("btn_resolution")
        self.gridLayout.addWidget(self.btn_resolution, 1, 0, 1, 1)
        self.tabWidget.addTab(self.first_page, "")
        self.second_page = QtWidgets.QWidget()
        self.second_page.setObjectName("second_page")
        self.tabWidget.addTab(self.second_page, "")
        self.third_page = QtWidgets.QWidget()
        self.third_page.setObjectName("third_page")
        self.tabWidget.addTab(self.third_page, "")
        self.fourth_page = QtWidgets.QWidget()
        self.fourth_page.setObjectName("fourth_page")
        self.tabWidget.addTab(self.fourth_page, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "痒痒鼠助手"))
        self.resolution_label.setText(_translate("MainWindow", "TextLabel"))
        self.btn_resolution.setText(_translate("MainWindow", "分辨率检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.first_page), _translate("MainWindow", "主页面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.second_page), _translate("MainWindow", "魂十"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.third_page), _translate("MainWindow", "魂土"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fourth_page), _translate("MainWindow", "突破"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
