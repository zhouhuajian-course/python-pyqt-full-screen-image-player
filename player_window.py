"""
播放器窗口

@author: zhouhuajian
@version: v1.0
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


class PlayerWindow(QLabel):
    """播放器窗口"""

    def __init__(self, playerMainWindow):
        """初始化"""
        super().__init__(parent=playerMainWindow)
        self.setWindowFlag(Qt.WindowType.Window)
        self.playerMainWindow = playerMainWindow

    def play(self, allImagePaths: list):
        """播放图片"""
        print("正在播放图片...")
        self.show()
        print(allImagePaths)

