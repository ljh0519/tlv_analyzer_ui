import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QMenu, QDialog,
                             QMessageBox, QApplication,
                             QAction, qApp, QLabel, QFileDialog,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QGroupBox, QGridLayout, QDesktopWidget,
                             QDockWidget, QSplitter)
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
        self.__menubar_ = UI_menuBar()
        self.setMenuBar(self.__menubar_)
        # mainLayout = QGridLayout()
        # # mainLayout.addWidget(self.__tlvInfoGB_, 0, 0, 10, 1)
        # # mainLayout.addWidget(self.__videoGB_, 0, 1, 8, 6)
        # # mainLayout.addWidget(self.__audioGB_, 8, 1, 2, 6)
        # # mainLayout.addWidget(self.__tlvPkgListGB_, 0, 7, 10, 3)
        # mainLayout.addWidget(self.__hsplitter_, 0, 0, 10, 1)
        # mainLayout.addWidget(self.__videoGB_, 0, 1, 8, 6)
        # mainLayout.addWidget(self.__audioGB_, 8, 1, 2, 6)
        # mainLayout.addWidget(self.__tlvPkgListGB_, 0, 7, 10, 3)
        # mainLayout.setRowStretch(1, 1)
        # mainLayout.setRowStretch(2, 1)
        # mainLayout.setColumnStretch(0, 1)
        # mainLayout.setColumnStretch(1, 1)
        # w = QWidget()
        # w.setLayout(mainLayout)
        self.setCentralWidget(self.__hsplitter_)

        self.resize(self.__winResolution_[0], self.__winResolution_[1])
        self.setWindowTitle('tlv分析工具')
        self.__center()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __initTlvInfoLayout(self):
        # hlayout = QHBoxLayout()
        # hlayout.addStretch(1)
        # hlayout.addWidget()
        # hlayout.addStretch(1)

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addWidget(QLabel('TLV INFO'))
        vlayout.addStretch(1)
        tlvInfo = QGroupBox("TLV INFO")
        tlvInfo.setLayout(vlayout)
        self.__hsplitter_.addWidget(tlvInfo)

    def __initTlvPkgListLayout(self):
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addWidget(QLabel('TLV Package'))
        vlayout.addStretch(1)
        tlvPkgList = QGroupBox("TLV Package")
        tlvPkgList.setLayout(vlayout)
        self.__hsplitter_.addWidget(tlvPkgList)

    def __initVideoLayout(self):
        video = UI_video()
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


class UI_video(QGroupBox):
    __images_ = None

    def __init__(self):
        super(UI_video, self).__init__()
        self.__initUI()

    def __initUI(self):
        #C:\Users\Li\Pictures\Tieba\test.jpg
        self.__images_ = QPixmap('C:\\Users\\Li\\Pictures\\Tieba\\test.jpg')
        self.__videoLabel_ = QLabel()
        self.__videoLabel_.setPixmap(self.__images_)
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(self.__videoLabel_)
        hlayout.addStretch(1)

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        vlayout.addStretch(1)
        video = QGroupBox("Video Replay")
        video.setMinimumSize(320, 240)
        # video.setGeometry(0,0, 320, 240)
        video.setLayout(vlayout)

    def resizeEvent(self, e: QResizeEvent) -> None:
        if self.__images_ is None:
            return
        w = e.size().width()
        h = e.size().height()
        image = self.resizeFrame(w, h, self.__images_)
        pixmap = QPixmap.fromImage(image)
        self.__videoLabel_.setPixmap(pixmap)
        QWidget.resizeEvent(self, e)

    def resizeFrame(self, w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)

        return pil_image.scaled(width, height)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tlv_analyzer = UI_mainWindow()
    tlv_analyzer.show()
    sys.exit(app.exec_())
