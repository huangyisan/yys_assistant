from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QRunnable,QThreadPool,pyqtSlot
import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from ui_yyswindow import Ui_MainWindow
import win32_func,game_func
from ui_pos_config import Ui_pos_config
from project_settings import yys_config_path
from game import soul

from configparser import ConfigParser
import importlib
import os
import signal


class AppContext(ApplicationContext):

    def run(self):
        window = YYSWindow()
        window.show()
        return self.app.exec_()

class YYSWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_MainWindow()

        self.__ui.setupUi(self)

        # set default tab "main page"
        self.__ui.tabWidget.setCurrentIndex(0)

        # radio default checked
        self.__ui.btn_radio_left.setChecked(True)
        self.__ui.btn_radio_leader_yes.setChecked(True)
        self.__ui.btn_radio_auto_no.setChecked(True)
        self.__ui.btn_radio_reward_yes.setChecked(True)
        self.__ui.checkbox_none_pos.setChecked(True)

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
        pos_name_list = [v for k,v in cfg.items('pos_name')]
        pos_name_list = filter(lambda x:x.startswith('判') or x.startswith('点'), pos_name_list)
        self.__ui.combobox_pixel_pos.addItems(pos_name_list)

        # 初始化开始脚本按钮
        self.__ui.btn_soul_start.setText('配置检测')

        # initial thread pool
        self.threadpool = QThreadPool()

        # 点击之类逻辑
        self.__ui.btn_move.clicked.connect(self.click_btn_move)
        self.__ui.btn_collect_piexl.clicked.connect(self.get_mouse_pos_pixel)
        self.__ui.btn_pos_list.clicked.connect(self.get_pos_list_config)
        self.__ui.btn_pos_save.clicked.connect(self.save_list_pos)
        self.__ui.btn_count_save.clicked.connect(self.save_exec_count)
        self.__ui.btn_soul_start.clicked.connect(self.start_soul)
        # self.__ui.btn_soul_start.clicked.connect(self.start_soul_process)
        self.__ui.btn_soul_stop.clicked.connect(self.stop_soul)

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

    def get_exec_count(self):
        '''
        初始化获取config.ini中exec_count的值
        :return:
        '''
        exec_count = cfg.get('count','exec_count')
        return int(exec_count)

    def lock_items_soul(self):
        self.__ui.groupbox_beforebattle.setEnabled(False)
        self.__ui.groupbox_duringbattle.setEnabled(False)
        self.__ui.groupbox_other.setEnabled(False)
        self.__ui.groupbox_execcout.setEnabled(False)

    def release_items_soul(self):
        self.__ui.groupbox_beforebattle.setEnabled(True)
        self.__ui.groupbox_duringbattle.setEnabled(True)
        self.__ui.groupbox_other.setEnabled(True)
        self.__ui.groupbox_execcout.setEnabled(True)



    def release_items_soul_stop(self):
        self.__ui.groupbox_beforebattle.setEnabled(True)
        self.__ui.groupbox_duringbattle.setEnabled(True)
        self.__ui.groupbox_other.setEnabled(True)
        self.__ui.groupbox_execcout.setEnabled(True)
        self.__ui.btn_soul_start.setEnabled(True)


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
        team_leader = self.__ui.btn_radio_leader_yes.isChecked()
        auto = self.__ui.btn_radio_auto_yes.isChecked()
        reward = self.__ui.btn_radio_reward_yes.isChecked()

        if self.__ui.btn_soul_start.text() == '配置检测':
            # 让game_func重新读取config.ini中dry_run
            importlib.reload(game_func)
            # 重新引入当前内存中pos配置信息
            self.reload_config()

            code, info = soul(focus=focus, exec_count=exec_count, team_leader=team_leader, auto=auto, reward=reward, dry_run=True)
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
            # p = multiprocessing.Process(target=soul,kwargs={'dry_run':False})
            p = Worker(fn=soul, focus=focus, exec_count=exec_count, team_leader=team_leader, auto=auto, reward=reward, dry_run=False)
            # p = Worker(fn=soul,kwargs={'focus':focus, 'exec_count':exec_count, 'team_leader':team_leader, 'auto':auto, 'reward':reward, 'dry_run':False})
            # p = multiprocessing.Process(target=soul,kwargs={'focus':focus, 'exec_count':exec_count, 'team_leader':team_leader, 'auto':auto, 'reward':reward, 'dry_run':False})
            self.threadpool.start(p)

            # 将子进程赋予self.child_pid变量
            # self.child_pid = p.pid
            self.__ui.btn_soul_start.setText('挂机中...')
            self.lock_items_soul()
            self.__ui.btn_soul_start.setEnabled(False)
            self.__ui.btn_soul_stop.setText('停止挂机')

    def stop_soul(self):
        if self.__ui.btn_soul_stop.text() == '停止挂机':
            if self.child_pid is None:
                self.showMessageBox(title='提示', message='当前没有执行挂机任务', icon=QMessageBox.Information)
            else:
                try:
                    os.kill(self.child_pid,signal.SIGTERM)
                except OSError:
                    pass
                self.child_pid = None
                cfg.set('dry_run','flag','1')
                with open(config_file, 'w', encoding='utf-8') as configfile:
                    cfg.write(configfile)
                self.showMessageBox(title='提示', message='已停止挂机', icon=QMessageBox.Information)
                self.__ui.btn_soul_start.setText('配置检测')
                self.release_items_soul_stop()
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

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

if  __name__ == "__main__":
    appctxt = AppContext()

    # 载入 config.ini 配置文件
    cfg = ConfigParser()
    config_file = yys_config_path
    cfg.read(config_file, encoding='utf-8')
    exit_code = appctxt.run()
    sys.exit(exit_code)

    # app = QApplication(sys.argv)     #创建app，用QApplication类
    # myWidget=YYSWindow()
    # myWidget.show()
    # sys.exit(app.exec_())
