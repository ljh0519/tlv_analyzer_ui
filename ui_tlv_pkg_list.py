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
        self.setMinimumWidth(300)
        self.setStyleSheet("QScrollArea{border: none;}")
        self.setWidgetResizable(True)
        group = QGroupBox(text)
        self.setWidget(group)
        self.__gvlay__ = QVBoxLayout()
        self.__gvlay__.setSpacing(0)
        self.__gvlay__.setContentsMargins(1, 1, 1, 1)
        group.setLayout(self.__gvlay__)

    def insertTlvPkgItem(self, title: str, text: str, color: str):
        box = CollapsibleBox(title)
        box.setAutoFillBackground(True)
        self.__gvlay__.addWidget(box)
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

    def changeTlvPkgItemState(self):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = QMainWindow()

    splitter = QSplitter(QtCore.Qt.Horizontal)
    splitter.setChildrenCollapsible(False)  # 拉动分割器至最小，被分割部分不会消失
    splitter.setAutoFillBackground(True)  # 分割器随主窗口大小自适应变化
    w.setCentralWidget(splitter)

    qw = QWidget()
    qw.setObjectName("Collapsible Demo")
    splitter.addWidget(qw)

    scroll = UITlvPkgList('ascacsac')
    splitter.addWidget(scroll)
    for i in range(30):
        scroll.insertTlvPkgItem("Collapsible Box Header-{}".format(i), '''this is an example!
this is an apple!
this is a banana!
this is a pen!
end''', '#999999')

    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())