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

# from __future__ import division
# import sys
# from PyQt5.QtWidgets import *
# from math import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *


# class Form(QDialog):
#     def __init__(self, text: str, parent=None):
#         super(Form, self).__init__(parent)
#         self.browser = QTextBrowser()
#         self.browser.setText(text)
#         self.click = QPushButton('OK')
#         layout = QVBoxLayout()
#         layout.addWidget(self.browser)
#         layout.addWidget(self.click)
#         self.setLayout(layout)
#         self.click.clicked.connect(self.updateUi)
#         # self.connect(self.click, SIGNAL("clicked()"), )
#         self.setWindowTitle("Calculate")
#
#     def updateUi(self):
#         self.browser.append("%s" % 'This is a test')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     form = Form('hehe')
#     form.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtCore import pyqtSignal, QObject
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
#
# class Communicate(QObject):
#
#     closeApp = pyqtSignal()
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Emit signal')
#         self.show()
#
#
#     def mousePressEvent(self, event):
#
#         self.c.closeApp.emit()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# from PyQt5.QtWidgets import *
# import sys
#
# class Window(QWidget):
#
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QVBoxLayout()
#         availSize = QDesktopWidget().availableGeometry()
#         self.setLayout(layout)
#         self.resize(availSize.width()*0.5, availSize.height()*0.5)
#
#         # Add toolbar and items
#         toolbox = QToolBox()
#         layout.addWidget(toolbox)
#         toolbox.addItem(QLabel(), "Students")
#         toolbox.addItem(QLabel(), "Teachers")
#         toolbox.addItem(QLabel(), "Directors")
#
#         # toolbox.setFrameShadow()
#         # layout = toolbox.layout()
#         # toolbox.setFrameShape(QToolBox.StyledPanel)
#         # show number of items
#         # print(toolbox.count())
#
#         # disable tab
#         # toolbox.setItemEnabled(0, False)
#
#         # mouseover tooltip
#         toolbox.setItemToolTip(0, "This is a tooltip")
#
#         # tests if items are enabled
#         # print(toolbox.isItemEnabled(0))
#         # print(toolbox.isItemEnabled(1))
#
#         # insert item
#         item = QLabel()
#         toolbox.insertItem(1, item, "Python")
#
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QSplitter, QToolButton,
                             QScrollArea, QSizePolicy, QFrame,
                             QVBoxLayout, QGroupBox, QApplication,
                             QMainWindow, QTextBrowser, QLabel)


class CollapsibleBox(QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet('''QToolButton{ 
        border: none;
        list-style-type: decimal;
        }''')
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.clicked.connect(self.on_clicked)

        self.content_area = QScrollArea()
        self.content_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.content_area.setFrameShape(QFrame.NoFrame)
        self.content_area.setHidden(True)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if checked else QtCore.Qt.RightArrow
        )
        if checked:
            self.content_area.setHidden(False)
        else:
            self.content_area.setHidden(True)

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)


class UITlvPkgList(QScrollArea):
    def __init__(self, text: str):
        super(UITlvPkgList, self).__init__()
        self.__initUI(text)

    def __initUI(self, text: str):
        group = QGroupBox(text)
        self.setWidget(group)
        self.__gvlayout_ = QVBoxLayout()
        self.__gvlayout_.setSpacing(0)
        self.__gvlayout_.setContentsMargins(1, 1, 1, 1)
        group.setLayout(self.__gvlayout_)

    def insertTlvPkgItem(self, title: str, text: str, color: str):
        box = CollapsibleBox("Collapsible Box Header-{}".format(i))
        box.setAutoFillBackground(True)


    def changeTlvPkgItemState(self):
        pass

    # def

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = QMainWindow()

    splitter = QSplitter(QtCore.Qt.Horizontal)
    splitter.setChildrenCollapsible(False)  # 拉动分割器至最小，被分割部分不会消失
    splitter.setAutoFillBackground(True)  # 分割器随主窗口大小自适应变化
    w.setCentralWidget(splitter)

    qw = QWidget()
    qw.setObjectName('main_widget')
    splitter.addWidget(qw)

    scroll = QScrollArea()
    scroll.setMinimumWidth(300)
    scroll.setStyleSheet("QScrollArea{border: none;}")
    scroll.setWidgetResizable(True)
    splitter.addWidget(scroll)

    group = QGroupBox("Collapsible Demo")
    scroll.setWidget(group)

    vlay = QVBoxLayout()
    vlay.setSpacing(0)
    vlay.setContentsMargins(1, 1, 1, 1)
    for i in range(30):
        box = CollapsibleBox("Collapsible Box Header-{}".format(i))
        box.setAutoFillBackground(True)
        vlay.addWidget(box)
        lay = QVBoxLayout()
        text_brw = QLabel()
        # text_brw.setAlignment()
        text_brw.setText('''this is an example!
this is an apple!
this is a banana!
this is a pen!
end''')
        lay.addWidget(text_brw)
        box.setContentLayout(lay)

    group.setLayout(vlay)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())