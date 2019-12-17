import sys
from PyQt5.QtWidgets import  QWidget, QApplication, QMainWindow, QMessageBox, QDialog, QStyleFactory
from ui_yyswindow import Ui_MainWindow
from yys_functions import win32_func
from yys_configurations import config
from ui_pos_config import Ui_pos_config

class YYSWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_MainWindow()

        self.__ui.setupUi(self)


        # radio default checked
        self.__ui.btn_radio_left.setChecked(True)

        # 程序启动后加载执行的一些任务
        self.get_screen_resolution()

        # 追加像素点combbox内容
        self.__ui.combobox_pixel_pos.addItems(config.default_combobox_pixel_pos)
        # 设定combobox的默认值
        self.__ui.combobox_pixel_pos.setCurrentIndex(1)

        # 点击之类逻辑
        self.__ui.btn_move.clicked.connect(self.click_Btn_move)
        # self.__ui.btn_collect_piexl.clicked.connect(self.get_current_combobox_value)
        self.__ui.btn_collect_piexl.clicked.connect(self.get_mouse_pos_pixel)
        self.__ui.btn_pos_list.clicked.connect(self.pos_list_config)
        self.__ui.btn_pos_save.clicked.connect(self.list_pos_save)


    def get_screen_resolution(self):
        '''
        获取当前屏幕分辨率
        :return: None
        '''
        resolution = win32_func.get_screen_resolution()
        text = '当前屏幕分辨率为: {}'.format(':'.join(str(v) for v in resolution))
        self.__ui.resolution_label.setText(text)
        # self.__ui.resolution_label.setText('1111')

    def showMessageBox(self, title, message,icon):
        '''
        弹窗组件
        :param title:
        :param message:
        :param icon:
        :return:
        '''
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(icon)
        msgBox.exec_()

    def click_Btn_move(self):
        '''
        窗口移动，根据checkbox选择进行左移，或者右移动
        :return:
        '''
        line_handle_text = self.__ui.line_handle.text()
        if line_handle_text:
            if self.__ui.btn_radio_left.isChecked():
                win32_func.window_move_left(file_name=line_handle_text)

            elif self.__ui.btn_radio_right.isChecked():
                win32_func.window_move_right(file_name=line_handle_text)
        else:
            # 错误弹窗调用
            self.showMessageBox(title='错误', message='未输入句柄名称',icon=QMessageBox.Critical)

    def get_mouse_pos_pixel(self):
        '''
        采集鼠标当前指向坐标rgb颜色，并且将combobox中的值作为key，坐标作为value，进行存储
        :return:
        '''
        res = win32_func.get_mouse_pos_pixel()
        pos = res[-1]
        rgb = res[0:2]
        self.__ui.label_piexl.setText('采集像素点坐标为：{}'.format(pos))
        self.__ui.label_piexl.setStyleSheet("color: rgb{};".format(rgb))
        config.pixel_info_dict[self.__ui.combobox_pixel_pos.currentText()]=res

    def pos_list_config(self):
        '''
        展现当前运行状态中，pos的位置和采取到的颜色
        :return:
        '''
        pos_config = YYS_pos_config(self)
        pos_config.show()

    def list_pos_save(self):
        '''
        将当前内存中的pos列表进行保存到磁盘中
        :return:
        '''
        self.showMessageBox(title='提示', message='保存成功', icon=QMessageBox.Information)


class YYS_pos_config(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_pos_config()
        self.__ui.setupUi(self)

        # 获取pos配置列表
        pos_str = '采集点信息如下:\n'
        for k,v in config.pixel_info_dict.items():
            pos_str += '{0}, 坐标为:{1}, RGB为:{2}\n'.format(k,v[-1],v[0:3])
        pos_str += '\n\n\nRGB Online: https://www.colorspire.com/rgb-color-wheel/'
        self.__ui.text_pos_config.setText(pos_str)
        self.__ui.text_pos_config.setReadOnly(True)

        # 关闭自身window
        self.__ui.btn_ok.clicked.connect(self.close)


if  __name__ == "__main__":

    app = QApplication(sys.argv)     #创建app，用QApplication类
    myWidget=YYSWindow()
    myWidget.show()
    sys.exit(app.exec_())

