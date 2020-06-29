import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QMenu, QDialog,
                             QMessageBox, QApplication,
                             QAction, qApp, QLabel, QFileDialog,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QGroupBox, QGridLayout, QDesktopWidget,
                             QDockWidget, QSplitter, QFormLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QResizeEvent
from ui_menubar import UI_menuBar


class UI_mainWindow(QMainWindow):
    __tlvInfoGB_ = None
    __tlvPkgListGB_ = None
    __videoGB_ = None
    __videoLabel_ = None
    __audioGB_ = None
    __audioLabel_ = None
    __menubar_ = None
    __winResolution_ = (1280, 720)

    def __init__(self):
        super().__init__()
        self.__vsplitter_ = QSplitter(Qt.Vertical)
        self.__hsplitter_ = QSplitter(Qt.Horizontal)
        self.__initTlvInfoLayout()
        self.__initVideoLayout()
        self.__initAudioLayout()
        self.__initTlvPkgListLayout()
        self.__initMainWindow()

    def __initMainWindow(self):
        availGeometry = QDesktopWidget().availableGeometry()
        self.resize(availGeometry.width()*0.7, availGeometry.height()*0.7)
        self.__center()

        self.__menubar_ = UI_menuBar()
        self.setMenuBar(self.__menubar_)
        self.setCentralWidget(self.__hsplitter_)
        self.setWindowTitle('tlv分析工具')

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __initTlvInfoLayout(self):
        tlvinfo = QLabel('FILE INFO')
        tlvinfo.setFrameShape(QLabel.StyledPanel)
        flayout = QFormLayout()
        flayout.addRow(tlvinfo)
        tlvInfoGB = QGroupBox("TLV INFO")
        tlvInfoGB.setLayout(flayout)
        self.__hsplitter_.addWidget(tlvInfoGB)

    def __initTlvPkgListLayout(self):
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addWidget(QLabel('TLV Package'))
        vlayout.addStretch(1)
        tlvPkgList = QGroupBox("TLV Package")
        tlvPkgList.setLayout(vlayout)
        self.__hsplitter_.addWidget(tlvPkgList)

    def __initVideoLayout(self):
        label = UI_videoLabel()
        label.setMinimumSize(320, 240)
        # video.setGeometry(0,0, 320, 240)
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(label)
        hlayout.addStretch(1)
        vlayout = QVBoxLayout()
        # vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        # vlayout.addStretch(1)
        video = QGroupBox("Video Replay")
        video.setLayout(vlayout)
        self.__vsplitter_.addWidget(video)

    def __initAudioLayout(self):
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(QLabel('Audio Replay'))
        hlayout.addStretch(1)

        audio = QGroupBox("Audio Replay")
        audio.setLayout(hlayout)
        self.__vsplitter_.addWidget(audio)
        self.__vsplitter_.setSizes([420, 300])
        self.__hsplitter_.addWidget(self.__vsplitter_)


class UI_videoLabel(QLabel):
    __images_ = None

    def __init__(self):
        super(UI_videoLabel, self).__init__()
        self.__initUI()

    def __initUI(self):
        # C:\Users\Li\Pictures\Tieba\test.jpg
        self.__images_ = QPixmap('C:\\Users\\Li\\Pictures\\Tieba\\test.jpg')
        # self.__images_ = QPixmap("C:\\Users\\Li\\Pictures\\test.jpg")
        self.setPixmap(self.__images_)

    def resizeEvent(self, e: QResizeEvent) -> None:
        if self.__images_ is None:
            return
        pixmap = self.__resizeFrame(e.size().width(), e.size().height())
        self.setPixmap(pixmap)
        QWidget.resizeEvent(self, e)

    def __resizeFrame(self, w_box, h_box):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = self.__images_.width(), self.__images_.height() # 获取图像的原始大小
        f1 = 1.0 * w / h
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)

        return self.__images_.scaled(width, height, Qt.KeepAspectRatio)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tlv_analyzer = UI_mainWindow()
    tlv_analyzer.show()
    sys.exit(app.exec_())
