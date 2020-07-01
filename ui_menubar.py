import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QMenuBar, QDialog,
                             QMessageBox, QApplication,
                             QAction, qApp, QLabel, QFileDialog,
                             QHBoxLayout, QVBoxLayout, QDesktopWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class UIMenuBar(QMenuBar):
    __aboutText_ = '''
这是一个tlv分析工具，
用于分析tlv中缓存的RTP
数据：丢包，乱序等情况，
并将tlv中的RTP数据转
换成音视频数据播放出来。

      作者：lijiahao
'''
    # __cwd_ = os.getcwd()
    __itemDialog_ = None

    def __init__(self):
        super().__init__()

        self.__initMenu()
        self.__initAbout()

#public:
    def showTest(self):
        availGeometry = QDesktopWidget().availableGeometry()
        self.windows = QMainWindow()
        self.windows.setMenuBar(self)
        self.windows.resize(availGeometry.width()*0.5, availGeometry.height()*0.5)
        self.windows.setWindowTitle('tlv分析工具')
        self.windows.show()

#private:
    def __addActExit(self):
        exit_action = QAction('&退出', self)
        exit_action.setShortcut('Ctrl+Shift+Q')
        exit_action.setStatusTip('退出应用程序')
        exit_action.triggered.connect(qApp.quit)
        self.menubar_.addAction(exit_action)

    def __addActAbout(self):
        about_action = QAction('&关于...', self)
        about_action.setStatusTip('关于')
        about_action.triggered.connect(self.__onAboutDialog)
        self.aboutbar_.addAction(about_action)

    def __onAboutDialog(self):
        if self.__itemDialog_ is not None:
            self.__itemDialog_.destroy()
            self.__itemDialog_ = None

        self.__itemDialog_ = QDialog()
        self.__itemDialog_.resize(300, 150)
        self.__itemDialog_.setWindowTitle('关于')
        hlayout = QHBoxLayout()
        text = QLabel()
        text.setText(self.__aboutText_)
        hlayout.addStretch(1)
        hlayout.addWidget(text)
        hlayout.addStretch(1)

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        vlayout.addStretch(1)
        self.__itemDialog_.setLayout(vlayout)
        # 模态，只有关闭对话框，才能关闭主窗口
        self.__itemDialog_.setWindowModality(Qt.ApplicationModal)
        self.__itemDialog_.show()

    def __initAbout(self):
        self.aboutbar_ = self.addMenu('&关于')


        self.__addActAbout()

    def __initMenu(self):
        self.menubar_ = self.addMenu('&菜单')
        self.__addActOpenFile()
        self.__addActExit()

    def __addActOpenFile(self):
        open_file_action = QAction('&打开文件...', self)
        open_file_action.setShortcut('Ctrl+Shift+F')
        open_file_action.setStatusTip('打开目标文件')
        open_file_action.triggered.connect(self.__onFileDialog)
        self.menubar_.addAction(open_file_action)

    def __onFileDialog(self):
        self.__filePath_, fileType = QFileDialog().getOpenFileName(self
                                                                   , "选取tlv文件"
                                                                   , os.getcwd()
                                                                   , "All Files (*);;Tlv Files (*.tlv*)")

        if self.__filePath_ == '':
            return

        if self.__itemDialog_ is not None:
            self.__itemDialog_.destroy()
            self.__itemDialog_ = None

        self.__itemDialog_ = QDialog()
        self.__itemDialog_.resize(500, 80)
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
    ex = UIMenuBar()
    ex.showTest()
    sys.exit(app.exec_())