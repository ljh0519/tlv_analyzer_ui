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


from PyQt5 import QtCore, QtGui, QtWidgets


class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(text=title, checkable=True, checked=False)
        # self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        # self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea( maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_area.setHidden(True)

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        # self.toggle_animation.addAnimation(
        #     QtCore.QPropertyAnimation(self, b"minimumHeight")
        # )
        # self.toggle_animation.addAnimation(
        #     QtCore.QPropertyAnimation(self, b"maximumHeight")
        # )
        # self.toggle_animation.addAnimation(
        #     QtCore.QPropertyAnimation(self.content_area, b"maximumHeight")
        # )

    @QtCore.pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if not checked else QtCore.Qt.RightArrow
        )
        if checked is True:
            self.content_area.setHidden(True)
            # self.content_area.set
        else:
            self.content_area.setHidden(False)
        # self.toggle_animation.setDirection(
        #     QtCore.QAbstractAnimation.Forward
        #     if not checked
        #     else QtCore.QAbstractAnimation.Backward
        # )
        # self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        # collapsed_height = (
        #     self.sizeHint().height() - self.content_area.maximumHeight()
        # )
        # content_height = layout.sizeHint().height()
        # # for i in range(self.toggle_animation.animationCount()):
        # #     animation = self.toggle_animation.animationAt(i)
        # #     animation.setDuration(500)
        # #     animation.setStartValue(collapsed_height)
        # #     animation.setEndValue(collapsed_height + content_height)
        # #
        # content_animation = self.toggle_animation.animationAt(
        #     self.toggle_animation.animationCount() - 1
        # )
        # content_animation.setDuration(content_height)
        # content_animation.setStartValue(0)
        # content_animation.setEndValue(content_height)


if __name__ == "__main__":
    import sys
    import random

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()

    splitter = QSplitter(Qt.Horizontal)
    splitter.setChildrenCollapsible(False)  # 拉动分割器至最小，被分割部分不会消失
    splitter.setAutoFillBackground(True)  # 分割器随主窗口大小自适应变化
    w.setCentralWidget(splitter)

    group = QtWidgets.QGroupBox("Collapsible Demo")

    qw = QtWidgets.QWidget()
    qw.setObjectName('main_widget')
    splitter.addWidget(qw)

    scroll = QtWidgets.QScrollArea()
    splitter.addWidget(scroll)
    # scroll.setWidget(group)
    # gvlay = QVBoxLayout(scroll)
    # group.setLayout(gvlay)

    # content = QtWidgets.QWidget()
    # content.setAutoFillBackground(True)
    scroll.setWidget(group)
    scroll.setWidgetResizable(True)
    vlay = QtWidgets.QVBoxLayout()
    # hlay = QtWidgets.QHBoxLayout()
    vlay.setSpacing(0)
    vlay.setContentsMargins(0, 0, 0, 0)
    for i in range(30):
        box = CollapsibleBox("Collapsible Box Header-{}".format(i))
        box.setAutoFillBackground(True)
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()
        # for j in range(8):
        #     label = QtWidgets.QLabel("{}".format(j))
        #     color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
        #     label.setStyleSheet(
        #         "background-color: {}; color : white;".format(color.name())
        #     )
        #     label.setAlignment(QtCore.Qt.AlignCenter)
        #     lay.addWidget(label)
        text_brw = QTextBrowser()
        text_brw.setText('''this is an example!
this is an apple!
this is a banana!
this is a pen!
end''')
        text_brw.setFrameShape(QTextBrowser.NoFrame)
        lay.addWidget(text_brw)

        box.setContentLayout(lay)

    # vlay.addStretch()
    # hlay.addStretch(1)
    # hlay.addLayout(vlay)
    # hlay.addStretch(1)
    group.setLayout(vlay)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())