from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from settings import *


class Reader(QLabel):
    def __init__(self):
        super(Reader, self).__init__()
        self.mouse_drag_pos = None
        self.resize(1000, 100)
        self.setWindowTitle("NovelReader")  # 设置窗口名
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setText('正在加载')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 窗口无边框且置顶
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明
        self.setStyleSheet('QLabel{color:%s;}' % settings.color)
        font = QtGui.QFont()
        font.setFamily(settings.font)
        font.setPointSize(settings.fontSize)
        self.setFont(font)
        # 是否跟随鼠标
        self.is_follow_mouse = False

    def mousePressEvent(self, event):
        """鼠标左键按下时, 文字将和鼠标位置绑定"""
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        """鼠标移动, 则文字也移动"""
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        """鼠标释放时, 取消绑定"""
        self.is_follow_mouse = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
