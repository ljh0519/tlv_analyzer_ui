import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QMenu, QDialog,
                             QMessageBox, QApplication,
                             QAction, qApp, QLabel, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class tr_MenuBar(QMenu):
    __style_ = 'Fusion'
    __aboutText_ = '''
        这是一个tlv分析工具，
        用于分析tlv中缓存的RTP
        数据：丢包，乱序等情况，
        并将tlv中的RTP数据转
        换成音视频数据播放出来。
                  作者：环信
    '''
    __background_ = (1920, 1080)
    __winResolution_ = (1280, 720)
    __cwd_ = os.getcwd()
    __itemDialog_ = None

    def __init__(self, app):
        super().__init__()

        self.__application = app
        self.__initMenu()
        self.__initAbout()

#public:
    def showTest(self):
        self.windows = QMainWindow()
        self.windows.menuBar().addMenu(self.__Amenu)
        self.windows.menuBar().addMenu(self.__Aabout)
        self.windows.setGeometry(
                (self.__background_[0] - self.__winResolution_[0]) / 2,
                (self.__background_[1] - self.__winResolution_[1]) / 2,
                self.__winResolution_[0], self.__winResolution_[1])
        self.windows.setWindowTitle('tlv分析工具')
        self.windows.show()
        return self.__application.exec_()

#private:
    def __addActExit(self, ):
        exit_action = QAction('&退出', self)
        exit_action.setShortcut('Ctrl+Shift+Q')
        exit_action.setStatusTip('退出应用程序')
        exit_action.triggered.connect(self.__application.quit)
        self.__Amenu.addAction(exit_action)

    def __addActAbout(self):
        about_action = QAction('&关于...', self)
        about_action.setStatusTip('关于')
        about_action.triggered.connect(self.__onAboutDialog)
        self.__Aabout.addAction(about_action)

    def __onAboutDialog(self):
        if self.__itemDialog_ is None:
            self.__itemDialog_ = QDialog()

        # self.aboutDialog.setStyle(self.__style)
        self.__itemDialog_.setGeometry(
                (self.__background_[0] - self.__winResolution_[0]) / 2,
                (self.__background_[1] - self.__winResolution_[1]) / 2,
                300,150)
        self.__itemDialog_.setWindowTitle('关于')
        text = QLabel(self.__itemDialog_)
        text.setText(self.__aboutText_)
        # 模态，只有关闭对话框，才能关闭主窗口
        self.__itemDialog_.setWindowModality(Qt.ApplicationModal)
        self.__itemDialog_.show()

    def __initAbout(self):
        self.__Aabout = self.addMenu('&关于')
        self.__addActAbout()

    def __initMenu(self):
        self.__Amenu = self.addMenu('&菜单')
        self.__addActOpenFile()
        self.__addActExit()

    def __addActOpenFile(self):
        open_file_action = QAction('&打开文件...', self)
        open_file_action.setShortcut('Ctrl+Shift+F')
        open_file_action.setStatusTip('打开目标文件')
        open_file_action.triggered.connect(self.__onFileDialog)
        self.__Amenu.addAction(open_file_action)

    def __onFileDialog(self):
        self.__filePath_, fileType = QFileDialog().getOpenFileName(self
                                                                   , "选取tlv文件"
                                                                   , self.__cwd_
                                                                   , "All Files (*);;Tlv Files (*.tlv*)")
        if self.__itemDialog_ is None:
            self.__itemDialog_ = QDialog()

        self.__itemDialog_.setGeometry(
                (self.__background_[0] - self.__winResolution_[0]) / 2,
                (self.__background_[1] - self.__winResolution_[1]) / 2,
                300,150)
        self.__itemDialog_.setWindowTitle('文件路径')
        text = QLabel(self.__itemDialog_)
        if self.__filePath_ == '':
            text.setText('未获取到文件路径')
        else:
            text.setText(self.__filePath_)
        # 模态，只有关闭对话框，才能关闭主窗口
        self.__itemDialog_.setWindowModality(Qt.ApplicationModal)
        self.__itemDialog_.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = tr_MenuBar(app)
    ret = ex.showTest()
    sys.exit(ret)