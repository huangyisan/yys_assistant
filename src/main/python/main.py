from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QThread
import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog, QLabel
from PyQt5.QtGui import QPixmap
from ui_yyswindow import Ui_MainWindow
import win32_func, game_func
from ui_pos_config import Ui_pos_config
from ui_yysdonate import Ui_dialog_donate
from project_settings import yys_config_path
from game import soul

from configparser import ConfigParser
import importlib
from hashlib import md5


class AppContext(ApplicationContext):
    def run(self):
        window = YYSWindow()
        window.show()
        return self.app.exec_()


class YYSWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui = Ui_MainWindow()

        self.__ui.setupUi(self)

        # set default tab "main page"
        self.__ui.tabWidget.setCurrentIndex(0)

        # 程序启动后加载执行的一些任务
        # 获取当前屏幕分辨率
        self.get_screen_resolution()

        # 脚本执行次数从配置文件中读取
        self.__ui.spinbox_exec_count.setValue(self.get_exec_count())

        # 设定初始config.ini中dry_run flag的值为1
        cfg.set('dry_run', 'flag', '1')
        with open(config_file, 'w', encoding='utf-8') as configfile:
            cfg.write(configfile)

        # 载入本地配置到内存
        self.reload_config()

        self.child_pid = None

        # 追加像素点combbox内容
        pos_name_list = [v for k, v in cfg.items('pos_name')]
        pos_name_list = filter(lambda x: x.startswith('判') or x.startswith('点'), pos_name_list)
        self.__ui.combobox_pixel_pos.addItems(pos_name_list)

        # 初始化开始脚本按钮
        self.__ui.btn_soul_start.setText('配置检测')

        # 点击之类逻辑
        self.__ui.btn_move.clicked.connect(self.click_btn_move)
        self.__ui.btn_collect_piexl.clicked.connect(self.get_mouse_pos_pixel)
        self.__ui.btn_pos_list.clicked.connect(self.get_pos_list_config)
        self.__ui.btn_pos_save.clicked.connect(self.save_list_pos)
        self.__ui.btn_count_save.clicked.connect(self.save_exec_count)
        self.__ui.btn_soul_start.clicked.connect(self.start_soul)
        self.__ui.btn_soul_stop.clicked.connect(self.stop_soul)
        self.__ui.btn_donate.clicked.connect(self.get_donate_page)
        self.__ui.btn_how_to_soul.clicked.connect(self.get_help_info_soul)

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

    def get_exec_count(self):
        '''
        初始化获取config.ini中exec_count的值
        :return:
        '''
        exec_count = cfg.get('count', 'exec_count')
        return int(exec_count)

    def lock_items_soul(self):
        self.__ui.groupbox_running_mode.setEnabled(False)
        self.__ui.groupbox_duringbattle.setEnabled(False)
        self.__ui.groupbox_other.setEnabled(False)
        self.__ui.groupbox_execcout.setEnabled(False)

    def release_items_soul(self):
        self.__ui.groupbox_running_mode.setEnabled(True)
        self.__ui.groupbox_duringbattle.setEnabled(True)
        self.__ui.groupbox_execcout.setEnabled(True)

    def release_items_soul_stop(self):
        self.__ui.groupbox_running_mode.setEnabled(True)
        self.__ui.groupbox_duringbattle.setEnabled(True)
        self.__ui.groupbox_execcout.setEnabled(True)
        self.__ui.btn_soul_start.setEnabled(True)

    def get_help_info_soul(self):
        self.showMessageBox(title='帮助',
                            message='重要：请不要遮挡游戏窗口\n1. 请确保提前锁定阵容\n2. 确保开启自动战斗(战斗中左下角齿轮)\n3. 确保战斗后自动邀请(双开模式)\n4. 插画图鉴只选择"神乐插画"\n5. 无需开启樱饼自动\n6. 支持业原火等副本\n7. 如遇到无法暂停情况请按下ctrl+alt+del',
                            icon=QMessageBox.Information)

    def showMessageBox(self, title, message, icon):
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
            self.showMessageBox(title='错误', message='未输入句柄名称', icon=QMessageBox.Critical)

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

        game_func.pixel_info[self.__ui.combobox_pixel_pos.currentText()] = res

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

        for name, info in game_func.pixel_info.items():
            cfg.set('pixel_info', name, str(info))
        with open(config_file, 'w', encoding='utf-8') as configfile:
            cfg.write(configfile)
        self.showMessageBox(title='提示', message='保存成功', icon=QMessageBox.Information)

    def save_exec_count(self):
        count = self.__ui.spinbox_exec_count.value()
        cfg.set('count', 'exec_count', str(count))
        with open(config_file, 'w', encoding='utf-8') as configfile:
            cfg.write(configfile)
        if count:
            self.showMessageBox(title='提示', message='保存成功\n执行{}次'.format(count), icon=QMessageBox.Information)
        else:
            self.showMessageBox(title='提示', message='保存成功\n循环执行'.format(count), icon=QMessageBox.Information)

    def get_donate_page(self):
        donate_page = YYS_donate(self)
        if donate_page.check_qrcode():
            donate_page.pic.setPixmap(QPixmap("alipay_qrcode.png"))
            donate_page.pic.show()
            donate_page.show()
        else:
            self.showMessageBox(title='错误', message='二维码好像被海国人劫持了！', icon=QMessageBox.Critical)

    def check_soul_config_pos(self, func):
        '''
        检测御魂是否符合要执行挂机的配置pos. 返回值为0表示正常，1表示异常
        :return:
        '''

        # code,info = soul()
        isreward = self.__ui.btn_radio_reward_yes.isChecked()

        code, info = func()

        if code:
            self.showMessageBox(title='错误', message=info, icon=QMessageBox.Critical)
        else:
            self.showMessageBox(title='提示', message=info, icon=QMessageBox.Information)
            cfg.set('dry_run', 'flag', '0')
            with open(config_file, 'w', encoding='utf-8') as configfile:
                cfg.write(configfile)

    def get_shisheng_pos(self):
        '''
        获取式神位置点选
        :return:
        '''
        if self.__ui.checkbox_first_pos.isChecked():
            return 1
        elif self.__ui.checkbox_none_pos.isChecked():
            return 0
        elif self.__ui.checkbox_second_pos.isChecked():
            return 2
        elif self.__ui.checkbox_third_pos.isChecked():
            return 3
        elif self.__ui.checkbox_fourth_pos.isChecked():
            return 4
        elif self.__ui.checkbox_fifth_pos.isChecked():
            return 5

    def start_soul(self):
        '''
        启动御魂挂机脚本，
        :return:
        '''
        focus = self.get_shisheng_pos()

        exec_count = self.__ui.spinbox_exec_count.value()
        reward = self.__ui.btn_radio_reward_yes.isChecked()
        # 默认为single mode
        play_mode = self.__ui.checkbox_singleplay.isChecked()

        if self.__ui.btn_soul_start.text() == '配置检测':
            # 让game_func重新读取config.ini中dry_run
            importlib.reload(game_func)
            # 重新引入当前内存中pos配置信息
            self.reload_config()

            code, info = soul(focus=focus, play_mode=play_mode, exec_count=exec_count, reward=reward, dry_run=True)
            # code, info = soul(focus=focus,  dry_run=True)
            if code:
                self.showMessageBox(title='错误', message=info, icon=QMessageBox.Critical)
            else:
                self.showMessageBox(title='提示', message=info, icon=QMessageBox.Information)
                cfg.set('dry_run', 'flag', '0')
                with open(config_file, 'w', encoding='utf-8') as configfile:
                    cfg.write(configfile)
                self.lock_items_soul()
                self.__ui.btn_soul_start.setText('开始挂机')
                self.__ui.btn_soul_stop.setText('解除配置锁定')

        elif self.__ui.btn_soul_start.text() == '开始挂机':
            # 让game_func重新读取config.ini中dry_run
            importlib.reload(game_func)

            # 防止卡死，将soul进程单独fork出子进程
            self.p = MyThread(fn=soul, focus=focus, play_mode=play_mode, exec_count=exec_count, reward=reward,
                              dry_run=False)
            self.p.start()

            self.__ui.btn_soul_start.setText('挂机中...')
            self.lock_items_soul()
            self.__ui.btn_soul_start.setEnabled(False)
            self.__ui.btn_soul_stop.setText('停止挂机')

    def stop_soul(self):

        if self.__ui.btn_soul_stop.text() == '停止挂机':
            try:
                if self.p.isFinished():
                    self.showMessageBox(title='提示', message='当前没有执行挂机任务', icon=QMessageBox.Information)
                    self.__ui.btn_soul_start.setText('配置检测')
                    cfg.set('dry_run', 'flag', '1')
                    with open(config_file, 'w', encoding='utf-8') as configfile:
                        cfg.write(configfile)
                    self.release_items_soul_stop()
                else:
                    self.p.terminate()
                    self.p.wait()
                    cfg.set('dry_run', 'flag', '1')
                    with open(config_file, 'w', encoding='utf-8') as configfile:
                        cfg.write(configfile)
                    self.__ui.btn_soul_start.setText('配置检测')
                    self.release_items_soul_stop()
                    self.showMessageBox(title='提示', message='已停止挂机', icon=QMessageBox.Information)
            except AttributeError:
                self.showMessageBox(title='提示', message='当前没有执行挂机任务', icon=QMessageBox.Information)

        elif self.__ui.btn_soul_stop.text() == '解除配置锁定':
            self.release_items_soul()
            self.__ui.btn_soul_start.setText('配置检测')
            self.__ui.btn_soul_stop.setText('停止挂机')
            cfg.set('dry_run', 'flag', '1')
            with open(config_file, 'w', encoding='utf-8') as configfile:
                cfg.write(configfile)
            self.showMessageBox(title='提示', message='已解除配置锁定', icon=QMessageBox.Information)


class YYS_pos_config(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui = Ui_pos_config()
        self.__ui.setupUi(self)

        # 获取pos配置列表
        pos_str = '采集点信息如下:\n'
        for k, v in game_func.pixel_info.items():
            try:
                v = eval(v)
            except TypeError as e:
                pass
            pos_str += '{0}, 坐标为:{1}, RGB为:{2}\n'.format(k, v[-1], v[0:3])
        pos_str += '\n\n\nRGB Online: https://www.colorspire.com/rgb-color-wheel/'
        self.__ui.text_pos_config.setText(pos_str)
        self.__ui.text_pos_config.setReadOnly(True)

        # 关闭自身window
        self.__ui.btn_ok.clicked.connect(self.close)


class YYS_donate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui = Ui_dialog_donate()
        self.__ui.setupUi(self)
        self.pic = QLabel(self)
        self.__ui.btn_thanks.clicked.connect(self.close)

    def check_qrcode(self):
        '''
        检查二维码支付的md5值是否正确
        :return:
        '''
        with open("alipay_qrcode.png", 'rb') as f:
            data = f.read()
        qrcode_md5 = md5(data).hexdigest()
        if qrcode_md5 == 'f0804b815319ba98d1b1c36f32225ba4':
            return True
        else:
            return False

    def showMessageBox(self, title, message, icon):
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


class MyThread(QThread):
    '''
    通用型Thread入口
    '''

    def __init__(self, fn, *args, **kwargs):
        QThread.__init__(self)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.fn(*self.args, **self.kwargs)


if __name__ == "__main__":
    appctxt = AppContext()

    # 载入 config.ini 配置文件
    cfg = ConfigParser()
    config_file = yys_config_path
    cfg.read(config_file, encoding='utf-8')

    exit_code = appctxt.run()
    sys.exit(exit_code)
