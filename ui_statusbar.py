#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程

这个程序将创建状态栏。

作者：我的世界你曾经来过
博客：http://blog.csdn.net/weiaitaowang
最后编辑：2016年7月31日
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('这里是状态栏...')

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('状态栏')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())