"""
播放器主窗口

@author: zhouhuajain
@versoin: v1.0
"""
import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFileDialog


class PlayerMainWindow(QWidget):
    """播放器主窗口"""
    # 常见的图片后缀
    IMAGE_EXTENSIONS = {".JPG", ".JPEG", ".PNG", ".WEBP", ".BMP"}

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
        openFolderButton = QPushButton(QIcon("images/folder_icon.png"), "打开文件夹", clicked=self.openFolder)
        # openFolderButton.clicked.connect()
        openFolderButton.setFixedWidth(110)
        mainLayout.addWidget(openFolderButton)

    def openFolder(self):
        """打开文件夹"""
        # print("点击了打开文件夹")
        # 选择文件夹
        dirPath = QFileDialog.getExistingDirectory(parent=self)
        # print(dirPath)
        # print(repr(dirPath))
        # 如果用户没有选择文件夹，不做处理
        if not dirPath:
            return
        # 如果用户选择了文件夹，那么遍历文件夹里面的文件，获取图片文件的绝对路径
        filenameList = os.listdir(dirPath)
        allImagePaths = []
        for filename in filenameList:
            # 过滤非图片文件 .jpg .png
            fileExt = os.path.splitext(filename)[1]
            if (not fileExt) or (fileExt.upper() not in self.IMAGE_EXTENSIONS):
                continue
            imagePath = os.path.realpath(os.path.join(dirPath, filename))
            allImagePaths.append(imagePath)

        print(filenameList)
        print(allImagePaths)