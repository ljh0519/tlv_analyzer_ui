
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QResizeEvent
from PyQt5.QtWidgets import QLabel, QWidget


class UIVideoLabel(QLabel):
    __images_ = None

    def __init__(self):
        super(UIVideoLabel, self).__init__()
        self.__initUI()

    def __initUI(self):
        self.__images_ = QPixmap('./images/test.jpg')
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