"""
播放器主窗口

@author: zhouhuajain
@versoin: v1.0
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class PlayerMainWindow(QWidget):
    """播放器主窗口"""

    def __init__(self):
        """初始化"""
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化UI"""
        # 设置标题栏
        self.setWindowFlags(Qt.WindowType.Window |
                            Qt.WindowType.WindowTitleHint |
                            Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle("全屏图片播放器")
        self.setWindowIcon(QIcon("images/window_icon.png"))
        # 设置窗口大小
        self.setFixedSize(260, 100)
        # 打开文件夹按钮
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)
        openFolderButton = QPushButton(QIcon("images/folder_icon.png"), "打开文件夹")
        openFolderButton.setFixedWidth(110)
        mainLayout.addWidget(openFolderButton)