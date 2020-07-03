from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QToolButton,
                             QScrollArea, QSizePolicy, QFrame,
                             QVBoxLayout, QApplication,
                             QMainWindow, QLabel)


class CollapsibleBox(QWidget):
    def __init__(self, title: str, bg_color: str, parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.setAutoFillBackground(True)
        self.toggle_button = QToolButton(text=title, checkable=True, checked=False)
        style_sheet = "border: none;"
        style_sheet += "border-image: url(" + bg_color + ");"
        style_sheet += "font: bold 15px;"
        self.toggle_button.setStyleSheet(style_sheet)
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.setMinimumHeight(30)
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


class UITlvPkgList(QWidget):
    class PKG_LEVEL():
        NORMAL = ''                         # 正常
        LOSS = 'images/note_red.png'         # 丢包
        ORDER = 'images/note_yellow.png'     # 乱序

    def __init__(self, text: str):
        super(UITlvPkgList, self).__init__()
        self.__initUI(text)

    def __initUI(self, text: str):
        self.setMinimumWidth(320)
        self.setAutoFillBackground(True)
        v_lay = QVBoxLayout()
        self.__scroll_ = QScrollArea()
        self.__scroll_.setStyleSheet("QScrollArea{border: none;}")
        self.__scroll_.setWidgetResizable(True)
        title = QLabel()
        title.setText(text)
        title.setMinimumHeight(30)
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setAutoFillBackground(True)

        v_lay.addWidget(title)
        v_lay.addWidget(self.__scroll_)
        v_lay.setContentsMargins(5, 5, 5, 5)
        self.setLayout(v_lay)

        pkg_list = QWidget()
        pkg_list.setAutoFillBackground(True)
        self.__scroll_.setWidget(pkg_list)
        self.__pkg_list_vlay_ = QVBoxLayout()
        self.__pkg_list_vlay_.setSpacing(0)
        self.__pkg_list_vlay_.setContentsMargins(1, 1, 1, 1)
        pkg_list.setLayout(self.__pkg_list_vlay_)

    def insertTlvPkgItem(self, title: str, text: str, bg_color: str):
        box = CollapsibleBox(title, bg_color)
        self.__pkg_list_vlay_.addWidget(box)
        lay = QVBoxLayout()
        text_brw = QLabel()
        text_brw.setText(text)
        text_brw.setAlignment(QtCore.Qt.AlignCenter)        # 居中对齐
        lay.addWidget(text_brw)
        box.setContentLayout(lay)

    def changeTlvPkgItemState(self):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = QMainWindow()

    q = QWidget()
    w.setCentralWidget(q)

    vlay = QVBoxLayout()
    q.setLayout(vlay)
    scroll = UITlvPkgList('Tlv Pkg List')
    vlay.addWidget(scroll)
    for i in range(30):
        pkg_level = UITlvPkgList.PKG_LEVEL.NORMAL
        if i % 10 == 0:
            pkg_level = UITlvPkgList.PKG_LEVEL.LOSS
        elif i % 11 == 0:
            pkg_level = UITlvPkgList.PKG_LEVEL.ORDER
        scroll.insertTlvPkgItem("Collapsible Box Header-{}".format(i), '''this is an example!
this is an apple!
this is a banana!
this is a pen!
end''', pkg_level)

    w.resize(400, 480)
    w.show()
    sys.exit(app.exec_())