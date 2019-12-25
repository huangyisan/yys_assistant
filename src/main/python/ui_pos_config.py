# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pos_config.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pos_config(object):
    def setupUi(self, pos_config):
        pos_config.setObjectName("pos_config")
        pos_config.resize(458, 363)
        pos_config.setMinimumSize(QtCore.QSize(0, 0))
        pos_config.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(pos_config)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(pos_config)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.text_pos_config = QtWidgets.QTextEdit(self.groupBox)
        self.text_pos_config.setEnabled(True)
        self.text_pos_config.setObjectName("text_pos_config")
        self.gridLayout.addWidget(self.text_pos_config, 0, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(self.groupBox)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(pos_config)
        QtCore.QMetaObject.connectSlotsByName(pos_config)

    def retranslateUi(self, pos_config):
        _translate = QtCore.QCoreApplication.translate
        pos_config.setWindowTitle(_translate("pos_config", "采集点信息"))
        self.btn_ok.setText(_translate("pos_config", "OK"))
