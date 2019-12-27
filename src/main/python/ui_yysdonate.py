# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yys_donate.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_donate(object):
    def setupUi(self, dialog_donate):
        dialog_donate.setObjectName("dialog_donate")
        dialog_donate.resize(260, 310)
        self.btn_thanks = QtWidgets.QPushButton(dialog_donate)
        self.btn_thanks.setGeometry(QtCore.QRect(40, 260, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_thanks.setFont(font)
        self.btn_thanks.setObjectName("btn_thanks")

        self.retranslateUi(dialog_donate)
        QtCore.QMetaObject.connectSlotsByName(dialog_donate)

    def retranslateUi(self, dialog_donate):
        _translate = QtCore.QCoreApplication.translate
        dialog_donate.setWindowTitle(_translate("dialog_donate", "打赏"))
        self.btn_thanks.setText(_translate("dialog_donate", "Thanks"))

