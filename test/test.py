# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
#
# class SplitterExample(QWidget):
#     def __init__(self):
#         super(SplitterExample, self).__init__()
#         self.initUI()
#
#     def initUI( self ):
#         #设置全局布局为水平布局，设置标题与初始大小窗口
#         hbox = QHBoxLayout()
#         self.setWindowTitle("QSplitter例子")
#         self.setGeometry(300, 300, 300, 200)
#         #实例化QFrame控件
#         # topLeft.setVisible(True)
#         topLeft.setToolTip('hehe')
#         bottom = QFrame()
#         bottom.setFrameShape(QFrame.StyledPanel)
#         #实例化QSplitter控件并设置初始为水平方向布局
#         splitter1 = QSplitter(Qt.Horizontal)
#         textedit = QTextEdit()
#         #向Splitter内添加控件。并设置游戏的初始大小
#         splitter1.addWidget(topLeft)
#         splitter1.addWidget(textedit)
#         splitter1.setSizes([100, 200])
#         #实例化Splitter管理器，添加控件到其中，设置垂直方向
#         splitter2 = QSplitter(Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#         #设置窗体全局布局以及子布局的添加
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#
#     def __initTlvInfoLayout(self):
#         hlayout = QHBoxLayout()
#         hlayout.addStretch(1)
#         hlayout.addWidget(QLabel('TLV INFO'))
#         hlayout.addStretch(1)
#
#         vlayout = QVBoxLayout()
#         vlayout.addStretch(1)
#         vlayout.addLayout(hlayout)
#         vlayout.addStretch(1)
#         groupbox = QGroupBox("TLV INFO")
#         groupbox.setLayout(vlayout)
#         self.__topLeft_ = QFrame()
#         self.__topLeft_.setFrameShape(QFrame.StyledPanel)
#         self.__topLeft_.set
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = SplitterExample()
#     demo.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
#                              QFrame, QSplitter)
# from PyQt5.QtCore import Qt
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#
#         topleft = QFrame(self)
#         topleft.setFrameShape(QFrame.StyledPanel)
#
#         topright = QFrame(self)
#         topright.setFrameShape(QFrame.StyledPanel)
#
#         bottom = QFrame(self)
#         bottom.setFrameShape(QFrame.StyledPanel)
#
#         splitter1 = QSplitter(Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)
#         splitter1.setSizes([100, 200])
#
#         splitter2 = QSplitter(Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('窗口分隔')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import QWidget, QApplication
#
# class MyWindow(QWidget):
#     def __init__(self, parent=None):
#         super().__init__()
#         self.resize(300, 100)
#
#     def moveEvent(self, e):
#         print("x = {0}; y = {1}".format(e.pos().x(), e.pos().y()))
#         QWidget.moveEvent(self, e)
#
#     def resizeEvent(self, e):
#         print("w = {0}; h = {1}".format(e.size().width(),e.size().height()))
#         QWidget.resizeEvent(self, e)
#
# if __name__ == "main":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_() )

from __future__ import division
import sys
from PyQt5.QtWidgets import *
from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Form(QDialog):
    def __init__(self, text: str, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.browser.setText(text)
        self.click = QPushButton('OK')
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.click)
        self.setLayout(layout)
        self.click.clicked.connect(self.updateUi)
        # self.connect(self.click, SIGNAL("clicked()"), )
        self.setWindowTitle("Calculate")

    def updateUi(self):
        self.browser.append("%s" % 'This is a test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('hehe')
    form.show()
    sys.exit(app.exec_())