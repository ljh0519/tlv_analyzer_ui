import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget,
                             QGroupBox, QWidget, QTextBrowser,
                             QLabel, QSplitter, QPushButton,
                             QDialog, QFormLayout)
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
a=rtpmap:32 MPV/90000'''

class UITlvInfo(QGroupBox):
    __vlayout_ = None
    __sdp_ = None
    __codec_ = None

    def __init__(self, title: str):
        super(UITlvInfo, self).__init__(title)
        self.__initUI()

    def __initUI(self):
        self.setMinimumWidth(100)
        self.setFileInfoText(info)
        self.setTlvSdpText(sdp)
        self.setTlvCodecText('')
        self.setLayout(self.__vlayout_)

    def setFileInfoText(self, text: str):
        self.__flayout_ = QFormLayout()
        text_brw = QTextBrowser()
        text_brw.append(text)
        self.__flayout_.addWidget(text_brw)

    def setTlvSdpText(self, text):
        sdp_btn = QPushButton('Sdp Info')
        sdp_btn.clicked.connect(self.__TlvSdpMessage)

        sdp_msg = QTextBrowser()
        sdp_msg.setText(text)
        self.__sdpDialog_ = QDialog()
        self.__sdpDialog_.setWindowTitle('Sdp Info')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(sdp_msg)
        hlayout.addStretch(1)
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        vlayout.addStretch(1)
        self.__sdpDialog_.setLayout(vlayout)
        self.__flayout_.addWidget(sdp_btn)

    def __TlvSdpMessage(self):
        self.__sdpDialog_.show()

    def setTlvCodecText(self, text):
        codec_btn = QPushButton('Codec Info')
        codec_btn.clicked.connect(self.__TlvCodecMessage)

        codec_msg = QTextBrowser()
        codec_msg.setText(text)
        self.__CodecDialog_ = QDialog()
        self.__CodecDialog_.setWindowTitle('Codec Info')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(codec_msg)
        hlayout.addStretch(1)
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        vlayout.addStretch(1)
        self.__CodecDialog_.setLayout(vlayout)
        self.__flayout_.addWidget(codec_btn)

    def __TlvCodecMessage(self):
        self.__CodecDialog_.show()


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