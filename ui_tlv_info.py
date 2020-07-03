import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget,
                             QGroupBox, QWidget, QTextBrowser,
                             QLabel, QSplitter, QPushButton,
                             QDialog, QVBoxLayout, QHBoxLayout, QToolBox)
from PyQt5.QtCore import Qt


info = '''size = 1235123
pkg number = 456
video type = H264
audio type = opus'''

sdp = '''v=0
o=alice 2890844526 2890844526 IN IP4 host.anywhere.com
s=
c=IN IP4 host.anywhere.com
t=0 0
m=audio 49170 RTP/AVP 0
a=rtpmap:0 PCMU/8000
m=video 51372 RTP/AVP 31
a=rtpmap:31 H261/90000
m=video 53000 RTP/AVP 32
a=rtpmap:32 MPV/90000

o=alice 2890844526 2890844526 IN IP4 host.anywhere.com
s=
c=IN IP4 host.anywhere.com
t=0 0
m=audio 49170 RTP/AVP 0
a=rtpmap:0 PCMU/8000
m=video 51372 RTP/AVP 31
a=rtpmap:31 H261/90000
m=video 53000 RTP/AVP 32
a=rtpmap:32 MPV/90000'''

class UITlvInfo(QGroupBox):
    __codecinfo_ = None
    __sdpinfo_ = None
    __fileinfo_ = None

    def __init__(self, title: str):
        super(UITlvInfo, self).__init__(title)
        self.__initUI()

    def __initUI(self):
        vlayout = QVBoxLayout(self)
        self.__toolBox_ = QToolBox()
        vlayout.addWidget(self.__toolBox_)

        #  设置左侧导航栏 toolBox 初始化时的宽度
        self.__toolBox_.setStyleSheet("QToolBoxButton { min-width:180px}")
        # 设置左侧导航栏 toolBox 在左右拉拽时的最小宽度
        self.__toolBox_.setMinimumWidth(100)
        # 设置软件启动时默认打开导航栏的第几个 Item；这里设置的是打开第1个 Item。
        self.__toolBox_.setCurrentIndex(0)
        # self.__toolBox_.setFrameShape(QToolBox.Shape.StyledPanel) # 为toolbox增加边框
        # self.__toolBox_.set

        self.setFileInfoText(info)
        self.setTlvSdpText(sdp)
        self.setTlvCodecText('')

    def setFileInfoText(self, text: str):
        if self.__fileinfo_ is None:
            self.__fileinfo_ = QTextBrowser()
            self.__toolBox_.addItem(self.__fileinfo_, "File Info")

        self.__fileinfo_.setText(text)

    def setTlvSdpText(self, text):
        if self.__sdpinfo_ is None:
            self.__sdpinfo_ = QTextBrowser()
            self.__toolBox_.addItem(self.__sdpinfo_, 'Sdp Info')

        self.__sdpinfo_.setText(text)

    def setTlvCodecText(self, text):
        if self.__codecinfo_ is None:
            self.__codecinfo_ = QTextBrowser()
            self.__toolBox_.addItem(self.__codecinfo_, 'Codec Info')

        self.__codecinfo_.setText(text)


class testMainWin(QMainWindow):
    def __init__(self):
        super(testMainWin, self).__init__()
        availGeometry = QDesktopWidget().availableGeometry()
        self.resize(availGeometry.width()*0.5, availGeometry.height()*0.5)
        self.setWindowTitle('左边栏实验')
        q = QWidget()
        self.setCentralWidget(q)
        hlayout = QHBoxLayout(q)
        tlvInfo = UITlvInfo('TLV INFO')
        tlvInfo.setMaximumWidth(250)
        tlvInfo.setMinimumWidth(250)
        label = QLabel('heheheheheh')
        label.setAlignment(Qt.AlignCenter)
        hlayout.addWidget(tlvInfo)
        hlayout.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = testMainWin()
    window.show()
    sys.exit(app.exec_())