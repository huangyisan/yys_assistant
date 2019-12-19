import sys
from PyQt5.QtWidgets import  QWidget, QApplication, QMainWindow, QMessageBox, QDialog, QStyleFactory
from ui_yyswindow import Ui_MainWindow
from yys_functions import win32_func,game_func
from ui_pos_config import Ui_pos_config
from project_settings import yys_config_path
from yys_functions.game import soul

from configparser import ConfigParser
import importlib

class YYSWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_MainWindow()

        self.__ui.setupUi(self)

        # radio default checked
        self.__ui.btn_radio_left.setChecked(True)
        self.__ui.btn_radio_leader_yes.setChecked(True)
        self.__ui.btn_radio_auto_yes.setChecked(True)
        self.__ui.btn_radio_reward_yes.setChecked(True)

        # 程序启动后加载执行的一些任务
        # 获取当前屏幕分辨率
        self.get_screen_resolution()

        # 设定初始config.ini中dry_run flag的值为1
        cfg.set('dry_run', 'flag', '1')
        with open(config_file, 'w', encoding='utf-8') as configfile:
            cfg.write(configfile)

        # 载入本地配置到内存
        self.reload_config()

        # 追加像素点combbox内容
        pos_name_list = [v for k,v in cfg.items('pos_name')]
        self.__ui.combobox_pixel_pos.addItems(pos_name_list)

        # 初始化开始脚本按钮
        self.__ui.btn_soul_start.setText('配置检测')

        # 点击之类逻辑
        self.__ui.btn_move.clicked.connect(self.click_btn_move)
        self.__ui.btn_collect_piexl.clicked.connect(self.get_mouse_pos_pixel)
        self.__ui.btn_pos_list.clicked.connect(self.get_pos_list_config)
        self.__ui.btn_pos_save.clicked.connect(self.save_list_pos)
        self.__ui.btn_count_save.clicked.connect(self.save_exec_count)
        self.__ui.btn_config_check.clicked.connect(lambda: self.check_soul_config_pos(soul))
        self.__ui.btn_soul_start.clicked.connect(self.start_soul)

        # self.__ui.btn_soul_start.clicked.connect(self.check_simhun_running_config)





    def reload_config(self):
        '''
        重载配置文件
        :return:
        '''

        for i in cfg.items('pixel_info'):
            game_func.pixel_info[i[0]] = i[1]

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

    def click_btn_move(self):
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

        game_func.pixel_info[self.__ui.combobox_pixel_pos.currentText()]=res

    def get_pos_list_config(self):
        '''
        展现当前运行状态中，pos的位置和采取到的颜色
        :return:
        '''
        pos_config = YYS_pos_config(self)
        pos_config.show()

    def save_list_pos(self):
        '''
        将当前内存中的pos列表进行保存到磁盘中
        :return:
        '''

        for name,info in game_func.pixel_info.items():
            cfg.set('pixel_info',name,str(info))
        with open(config_file, 'w',encoding='utf-8') as configfile:
            cfg.write(configfile)
        self.showMessageBox(title='提示', message='保存成功', icon=QMessageBox.Information)

    def save_exec_count(self):
        count = self.__ui.spinbox_exec_count.value()
        cfg.set('count','exec_count',str(count))
        with open(config_file, 'w',encoding='utf-8') as configfile:
            cfg.write(configfile)
        if count:
            self.showMessageBox(title='提示', message='保存成功\n执行{}次'.format(count), icon=QMessageBox.Information)
        else:
            self.showMessageBox(title='提示', message='保存成功\n循环执行'.format(count), icon=QMessageBox.Information)

    def check_soul_config_pos(self,func):
        '''
        检测御魂是否符合要执行挂机的配置pos. 返回值为0表示正常，1表示异常
        :return:
        '''

        # code,info = soul()
        isteam_leader = self.__ui.btn_radio_leader_yes.isChecked()
        isauto = self.__ui.btn_radio_auto_yes.isChecked()
        isreward = self.__ui.btn_radio_reward_yes.isChecked()



        code,info= func()

        if code:
            self.showMessageBox(title='错误', message=info, icon=QMessageBox.Critical)
        else:
            self.showMessageBox(title='提示', message=info, icon=QMessageBox.Information)
            cfg.set('dry_run', 'flag', '0')
            with open(config_file, 'w', encoding='utf-8') as configfile:
                cfg.write(configfile)

    def start_soul(self):
        '''
        启动御魂挂机脚本，
        :return:
        '''
        isteam_leader = self.__ui.btn_radio_leader_yes.isChecked()
        isauto = self.__ui.btn_radio_auto_yes.isChecked()
        isreward = self.__ui.btn_radio_reward_yes.isChecked()


        if self.__ui.btn_soul_start.text() == '配置检测':
            # 让game_func重新读取config.ini中dry_run
            importlib.reload(game_func)
            # 重新引入当前内存中pos配置信息
            self.reload_config()

            code, info = soul()
            if code:
                self.showMessageBox(title='错误', message=info, icon=QMessageBox.Critical)
            else:
                self.showMessageBox(title='提示', message=info, icon=QMessageBox.Information)
                cfg.set('dry_run', 'flag', '0')
                with open(config_file, 'w', encoding='utf-8') as configfile:
                    cfg.write(configfile)
                self.__ui.btn_soul_start.setText('开始挂机')

        elif self.__ui.btn_soul_start.text() == '开始挂机':
            # 让game_func重新读取config.ini中dry_run
            importlib.reload(game_func)
            soul()
            cfg.set('dry_run','flag','1')
            with open(config_file, 'w', encoding='utf-8') as configfile:
                cfg.write(configfile)

class YYS_pos_config(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_pos_config()
        self.__ui.setupUi(self)

        # 获取pos配置列表
        pos_str = '采集点信息如下:\n'
        for k,v in game_func.pixel_info.items():
            try:
                v = eval(v)
            except TypeError as e:
                pass
            pos_str += '{0}, 坐标为:{1}, RGB为:{2}\n'.format(k,v[-1],v[0:3])
        pos_str += '\n\n\nRGB Online: https://www.colorspire.com/rgb-color-wheel/'
        self.__ui.text_pos_config.setText(pos_str)
        self.__ui.text_pos_config.setReadOnly(True)

        # 关闭自身window
        self.__ui.btn_ok.clicked.connect(self.close)


if  __name__ == "__main__":
    # 载入 config.ini 配置文件
    cfg = ConfigParser()
    config_file = yys_config_path
    cfg.read(config_file, encoding='utf-8')

    app = QApplication(sys.argv)     #创建app，用QApplication类
    myWidget=YYSWindow()
    myWidget.show()
    sys.exit(app.exec_())
