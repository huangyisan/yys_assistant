import sys
from PyQt5.QtWidgets import  QWidget, QApplication, QMainWindow
from ui_yyswindow import Ui_MainWindow
from yys_functions import win32_func

class YYSWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__ui=Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.btn_resolution.clicked.connect(self.click_Btn_resolution)

    def click_Btn_resolution(self):
        resolution = win32_func.get_screen_resolution()
        text = '当前屏幕分辨率为: {}'.format(':'.join(str(v) for v in resolution))
        self.__ui.resolution_label.setText(text)


if  __name__ == "__main__":

    app = QApplication(sys.argv)     #创建app，用QApplication类
    myWidget=YYSWindow()
    myWidget.show()
    sys.exit(app.exec_())

