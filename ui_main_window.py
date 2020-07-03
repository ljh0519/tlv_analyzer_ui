import sys
# import os
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel,
                              QVBoxLayout, QHBoxLayout,
                             QGroupBox,  QDesktopWidget, QSplitter)
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap, QResizeEvent
from ui_menu_bar import UIMenuBar
from ui_tlv_info import UITlvInfo
from ui_media_display import UIVideoLabel
from ui_tlv_pkg_list import UITlvPkgList


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
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.__vsplitter_ = QSplitter(Qt.Vertical)
        self.__vsplitter_.setChildrenCollapsible(False) # 拉动分割器至最小，被分割部分不会消失
        self.__vsplitter_.setAutoFillBackground(True) # 分割器随主窗口大小自适应变化
        self.__hsplitter_ = QSplitter(Qt.Horizontal)
        self.__hsplitter_.setChildrenCollapsible(False)
        self.__hsplitter_.setAutoFillBackground(True)
        self.__initTlvInfoLayout()
        self.__initVideoLayout()
        self.__initAudioLayout()
        self.__initTlvPkgListLayout()
        self.__initMainWindow()

    def __initMainWindow(self):
        availGeometry = QDesktopWidget().availableGeometry()
        self.resize(availGeometry.width()*0.7, availGeometry.height()*0.7)
        self.__center()

        self.__menubar_ = UIMenuBar()
        self.setMenuBar(self.__menubar_)
        self.setCentralWidget(self.__hsplitter_)
        self.setWindowTitle('tlv分析工具')

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __initTlvInfoLayout(self):
        tlvinfo = UITlvInfo('TLV INFO')
        tlvinfo.setMinimumWidth(250)
        self.__hsplitter_.addWidget(tlvinfo)

    def __initTlvPkgListLayout(self):
        self.__tlvpkglist_ = UITlvPkgList('Tlv Pkg List')
        for i in range(30):
            pkg_level = UITlvPkgList.PKG_LEVEL.NORMAL
            if i % 10 == 0:
                pkg_level = UITlvPkgList.PKG_LEVEL.LOSS
            elif i % 11 == 0:
                pkg_level = UITlvPkgList.PKG_LEVEL.ORDER
            self.__tlvpkglist_.insertTlvPkgItem("H264 RTP Header #{:<10d}".format(i), '''this is an example!
        this is an apple!
        this is a banana!
        this is a pen!
        end''', pkg_level)
        self.__hsplitter_.addWidget(self.__tlvpkglist_)

    def __initVideoLayout(self):
        label = UIVideoLabel()
        label.setMinimumSize(640, 480)
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    tlv_analyzer = UI_mainWindow()
    tlv_analyzer.show()
    sys.exit(app.exec_())
