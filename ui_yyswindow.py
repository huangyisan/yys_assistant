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
        MainWindow.resize(265, 484)
        MainWindow.setMinimumSize(QtCore.QSize(265, 387))
        MainWindow.setMaximumSize(QtCore.QSize(265, 999999))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 251, 451))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.first_page = QtWidgets.QWidget()
        self.first_page.setObjectName("first_page")
        self.groupBox = QtWidgets.QGroupBox(self.first_page)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.resolution_label = QtWidgets.QLabel(self.groupBox)
        self.resolution_label.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.resolution_label.setObjectName("resolution_label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.first_page)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 221, 91))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.line_handle = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_handle.setEnabled(True)
        self.line_handle.setGeometry(QtCore.QRect(10, 10, 201, 20))
        self.line_handle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.line_handle.setWhatsThis("")
        self.line_handle.setAccessibleName("")
        self.line_handle.setAccessibleDescription("")
        self.line_handle.setAutoFillBackground(False)
        self.line_handle.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_handle.setInputMask("")
        self.line_handle.setText("")
        self.line_handle.setMaxLength(30)
        self.line_handle.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_handle.setReadOnly(False)
        self.line_handle.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_handle.setClearButtonEnabled(False)
        self.line_handle.setObjectName("line_handle")
        self.btn_move = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_move.setGeometry(QtCore.QRect(10, 60, 201, 21))
        self.btn_move.setObjectName("btn_move")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 36, 102, 18))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_radio_left = QtWidgets.QRadioButton(self.layoutWidget)
        self.btn_radio_left.setObjectName("btn_radio_left")
        self.horizontalLayout_2.addWidget(self.btn_radio_left)
        self.btn_radio_right = QtWidgets.QRadioButton(self.layoutWidget)
        self.btn_radio_right.setObjectName("btn_radio_right")
        self.horizontalLayout_2.addWidget(self.btn_radio_right)
        self.groupBox_3 = QtWidgets.QGroupBox(self.first_page)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 221, 151))
        self.groupBox_3.setToolTip("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.combobox_pixel_pos = QtWidgets.QComboBox(self.groupBox_3)
        self.combobox_pixel_pos.setGeometry(QtCore.QRect(10, 30, 151, 22))
        self.combobox_pixel_pos.setObjectName("combobox_pixel_pos")
        self.btn_collect_piexl = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_collect_piexl.setGeometry(QtCore.QRect(170, 30, 41, 21))
        self.btn_collect_piexl.setObjectName("btn_collect_piexl")
        self.label_piexl = QtWidgets.QLabel(self.groupBox_3)
        self.label_piexl.setGeometry(QtCore.QRect(10, 80, 201, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_piexl.setFont(font)
        self.label_piexl.setText("")
        self.label_piexl.setObjectName("label_piexl")
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(10, 60, 201, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_pos_list = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_pos_list.setGeometry(QtCore.QRect(140, 120, 71, 21))
        self.btn_pos_list.setObjectName("btn_pos_list")
        self.btn_pos_save = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_pos_save.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.btn_pos_save.setObjectName("btn_pos_save")
        self.groupBox_6 = QtWidgets.QGroupBox(self.first_page)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 330, 221, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.spinbox_exec_count = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinbox_exec_count.setGeometry(QtCore.QRect(10, 20, 91, 22))
        self.spinbox_exec_count.setObjectName("spinbox_exec_count")
        self.btn_count_save = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_count_save.setGeometry(QtCore.QRect(140, 20, 71, 21))
        self.btn_count_save.setObjectName("btn_count_save")
        self.tabWidget.addTab(self.first_page, "")
        self.second_page = QtWidgets.QWidget()
        self.second_page.setObjectName("second_page")
        self.groupBox_4 = QtWidgets.QGroupBox(self.second_page)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 221, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn_radio_leader_yes = QtWidgets.QRadioButton(self.groupBox_4)
        self.btn_radio_leader_yes.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.btn_radio_leader_yes.setCheckable(True)
        self.btn_radio_leader_yes.setChecked(False)
        self.btn_radio_leader_yes.setObjectName("btn_radio_leader_yes")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_radio_leader_yes)
        self.btn_radio_leader_no = QtWidgets.QRadioButton(self.groupBox_4)
        self.btn_radio_leader_no.setGeometry(QtCore.QRect(130, 40, 89, 16))
        self.btn_radio_leader_no.setObjectName("btn_radio_leader_no")
        self.buttonGroup.addButton(self.btn_radio_leader_no)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.btn_radio_auto_yes = QtWidgets.QRadioButton(self.groupBox_4)
        self.btn_radio_auto_yes.setGeometry(QtCore.QRect(10, 80, 89, 16))
        self.btn_radio_auto_yes.setObjectName("btn_radio_auto_yes")
        self.btn_radio_auto_no = QtWidgets.QRadioButton(self.groupBox_4)
        self.btn_radio_auto_no.setGeometry(QtCore.QRect(130, 80, 89, 16))
        self.btn_radio_auto_no.setObjectName("btn_radio_auto_no")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 161, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.second_page)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 130, 221, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.checkbox_first_pos = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkbox_first_pos.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.checkbox_first_pos.setTristate(False)
        self.checkbox_first_pos.setObjectName("checkbox_first_pos")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.checkbox_first_pos)
        self.checkbox_second_pos = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkbox_second_pos.setGeometry(QtCore.QRect(80, 40, 51, 16))
        self.checkbox_second_pos.setObjectName("checkbox_second_pos")
        self.buttonGroup_2.addButton(self.checkbox_second_pos)
        self.checkbox_third_pos = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkbox_third_pos.setGeometry(QtCore.QRect(150, 40, 51, 16))
        self.checkbox_third_pos.setObjectName("checkbox_third_pos")
        self.buttonGroup_2.addButton(self.checkbox_third_pos)
        self.checkbox_fourth_pos = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkbox_fourth_pos.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.checkbox_fourth_pos.setObjectName("checkbox_fourth_pos")
        self.buttonGroup_2.addButton(self.checkbox_fourth_pos)
        self.checkbox_none_pos = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkbox_none_pos.setEnabled(True)
        self.checkbox_none_pos.setGeometry(QtCore.QRect(150, 60, 51, 16))
        self.checkbox_none_pos.setObjectName("checkbox_none_pos")
        self.buttonGroup_2.addButton(self.checkbox_none_pos)
        self.checkbox_fifth_pos = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkbox_fifth_pos.setGeometry(QtCore.QRect(80, 60, 51, 16))
        self.checkbox_fifth_pos.setObjectName("checkbox_fifth_pos")
        self.buttonGroup_2.addButton(self.checkbox_fifth_pos)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_3.setObjectName("label_3")
        self.groupbox_open_box = QtWidgets.QGroupBox(self.second_page)
        self.groupbox_open_box.setEnabled(True)
        self.groupbox_open_box.setGeometry(QtCore.QRect(10, 230, 221, 61))
        self.groupbox_open_box.setObjectName("groupbox_open_box")
        self.label_4 = QtWidgets.QLabel(self.groupbox_open_box)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 201, 16))
        self.label_4.setObjectName("label_4")
        self.btn_radio_open_yes = QtWidgets.QRadioButton(self.groupbox_open_box)
        self.btn_radio_open_yes.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.btn_radio_open_yes.setObjectName("btn_radio_open_yes")
        self.btn_radio_open_no = QtWidgets.QRadioButton(self.groupbox_open_box)
        self.btn_radio_open_no.setGeometry(QtCore.QRect(130, 40, 89, 16))
        self.btn_radio_open_no.setObjectName("btn_radio_open_no")
        self.groupBox_7 = QtWidgets.QGroupBox(self.second_page)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 310, 221, 61))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 201, 16))
        self.label_5.setObjectName("label_5")
        self.btn_radio_reward_yes = QtWidgets.QRadioButton(self.groupBox_7)
        self.btn_radio_reward_yes.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.btn_radio_reward_yes.setObjectName("btn_radio_reward_yes")
        self.btn_radio_reward_no = QtWidgets.QRadioButton(self.groupBox_7)
        self.btn_radio_reward_no.setGeometry(QtCore.QRect(130, 40, 89, 16))
        self.btn_radio_reward_no.setObjectName("btn_radio_reward_no")
        self.btn_soul_start = QtWidgets.QPushButton(self.second_page)
        self.btn_soul_start.setGeometry(QtCore.QRect(130, 390, 101, 23))
        self.btn_soul_start.setObjectName("btn_soul_start")
        self.btn_soul_stop = QtWidgets.QPushButton(self.second_page)
        self.btn_soul_stop.setGeometry(QtCore.QRect(10, 390, 101, 23))
        self.btn_soul_stop.setObjectName("btn_soul_stop")
        self.tabWidget.addTab(self.second_page, "")
        self.fourth_page = QtWidgets.QWidget()
        self.fourth_page.setObjectName("fourth_page")
        self.tabWidget.addTab(self.fourth_page, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "痒痒鼠助手"))
        self.resolution_label.setText(_translate("MainWindow", "当前屏幕分辨率未知"))
        self.line_handle.setToolTip(_translate("MainWindow", "痒痒鼠窗口名称"))
        self.line_handle.setPlaceholderText(_translate("MainWindow", "请输入句柄名称"))
        self.btn_move.setText(_translate("MainWindow", "移动"))
        self.btn_radio_left.setText(_translate("MainWindow", "左边"))
        self.btn_radio_right.setText(_translate("MainWindow", "右边"))
        self.groupBox_3.setTitle(_translate("MainWindow", "采点设定"))
        self.btn_collect_piexl.setToolTip(_translate("MainWindow", "请使用Alt+P进行采点"))
        self.btn_collect_piexl.setText(_translate("MainWindow", "Alt+&P"))
        self.btn_pos_list.setToolTip(_translate("MainWindow", "查看当前运行状态采点列表"))
        self.btn_pos_list.setText(_translate("MainWindow", "采点列表"))
        self.btn_pos_save.setToolTip(_translate("MainWindow", "保存采点信息到配置文件"))
        self.btn_pos_save.setText(_translate("MainWindow", "采点保存"))
        self.groupBox_6.setTitle(_translate("MainWindow", "执行次数"))
        self.spinbox_exec_count.setToolTip(_translate("MainWindow", "脚本执行次数，若0则一直执行直到退出"))
        self.btn_count_save.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.first_page), _translate("MainWindow", "主页面"))
        self.groupBox_4.setTitle(_translate("MainWindow", "战斗前"))
        self.btn_radio_leader_yes.setText(_translate("MainWindow", "是"))
        self.btn_radio_leader_no.setText(_translate("MainWindow", "否"))
        self.label.setText(_translate("MainWindow", "是否为队长？"))
        self.btn_radio_auto_yes.setText(_translate("MainWindow", "是"))
        self.btn_radio_auto_no.setText(_translate("MainWindow", "否"))
        self.label_2.setText(_translate("MainWindow", "是否开启自动？"))
        self.groupBox_5.setTitle(_translate("MainWindow", "战斗中"))
        self.checkbox_first_pos.setText(_translate("MainWindow", "一号"))
        self.checkbox_second_pos.setText(_translate("MainWindow", "二号"))
        self.checkbox_third_pos.setText(_translate("MainWindow", "三号"))
        self.checkbox_fourth_pos.setText(_translate("MainWindow", "四号"))
        self.checkbox_none_pos.setText(_translate("MainWindow", "否"))
        self.checkbox_fifth_pos.setText(_translate("MainWindow", "五号"))
        self.label_3.setText(_translate("MainWindow", "左起式神焦点"))
        self.groupbox_open_box.setTitle(_translate("MainWindow", "战斗后"))
        self.label_4.setText(_translate("MainWindow", "是否自动开箱？"))
        self.btn_radio_open_yes.setText(_translate("MainWindow", "是"))
        self.btn_radio_open_no.setText(_translate("MainWindow", "否"))
        self.groupBox_7.setTitle(_translate("MainWindow", "其他"))
        self.label_5.setText(_translate("MainWindow", "是否接受封印悬赏？"))
        self.btn_radio_reward_yes.setText(_translate("MainWindow", "是"))
        self.btn_radio_reward_no.setText(_translate("MainWindow", "否"))
        self.btn_soul_start.setToolTip(_translate("MainWindow", "先检测，再开始"))
        self.btn_soul_start.setText(_translate("MainWindow", "配置检测"))
        self.btn_soul_stop.setText(_translate("MainWindow", "停止挂机"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.second_page), _translate("MainWindow", "御魂"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fourth_page), _translate("MainWindow", "突破"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "帮助"))
