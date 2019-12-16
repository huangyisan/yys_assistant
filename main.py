import sys
from PyQt5.QtWidgets import  QWidget, QApplication, QMainWindow, QMessageBox
from ui_yyswindow import Ui_MainWindow
from yys_functions import win32_func

class YYSWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_MainWindow()
        self.__ui.setupUi(self)

        # radio default checked
        self.__ui.radioBtn_left.setChecked(True)

        # 程序启动后加载执行的一些任务
        self.get_screen_resolution()

        # logic
        self.__ui.btn_move.clicked.connect(self.click_Btn_move)

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
        yys_handle_text = self.__ui.YYS_Handle.text()
        if yys_handle_text:
            if self.__ui.radioBtn_left.isChecked():
                win32_func.window_move_left(file_name=yys_handle_text)

            elif self.__ui.radioBtn_rigth.isChecked():
                win32_func.window_move_right(file_name=yys_handle_text)
        else:
            # 错误弹窗调用
            self.showMessageBox(title='错误', message='未输入句柄名称',icon=QMessageBox.Critical)


if  __name__ == "__main__":

    app = QApplication(sys.argv)     #创建app，用QApplication类
    myWidget=YYSWindow()
    myWidget.show()
    sys.exit(app.exec_())

