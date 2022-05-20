"""
播放器窗口

@author: zhouhuajian
@version: v1.0
"""
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class PlayerWindow(QLabel):
    """播放器窗口"""

    def __init__(self, playerMainWindow):
        """初始化"""
        super().__init__(parent=playerMainWindow)
        self.setWindowFlag(Qt.WindowType.Window)
        self.playerMainWindow = playerMainWindow
        # 获取屏幕大小
        self.screenSize = self.screen().size()
        # 图片居中显示
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 定时器
        self.timer = QTimer(parent=self, timeout=self.playNextImage)
        self.timer.setInterval(3000)
        # self.timer.timeout.connect()

    def play(self, allImagePaths: list):
        """播放图片"""
        print("正在播放图片...")
        self.allImagePaths = iter(allImagePaths)
        # 调试 实现播放第一张图片
        # pixmap = QPixmap(allImagePaths[0]).scaled(self.screenSize, Qt.AspectRatioMode.KeepAspectRatio)
        # self.setPixmap(pixmap)
        # 隐藏主界面 全屏显示播放器
        self.playerMainWindow.hide()
        self.showFullScreen()
        # print(allImagePaths)
        # 播放第一张图片
        self.playNextImage()
        self.timer.start()

    def playNextImage(self):
        """播放下一张图片"""
        try:
            nextImagePath = next(self.allImagePaths)
            pixmap = QPixmap(nextImagePath).scaled(self.screenSize, Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(pixmap)
        except StopIteration:
            self.stop()

    def stop(self):
        """停止播放"""
        # 显示主界面 隐藏播放器窗口 停止定时器
        self.timer.stop()
        self.hide()
        self.playerMainWindow.show()


