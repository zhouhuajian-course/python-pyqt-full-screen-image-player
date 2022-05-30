"""
图片播放器 入口文件

@author: zhouhuajian
@version: v1.0
"""
from PyQt6.QtWidgets import QApplication

from player_main_window import PlayerMainWindow

if __name__ == '__main__':
    # 应用程序
    app = QApplication([])
    mainWindow = PlayerMainWindow()
    mainWindow.show()
    # 进入消息循环
    app.exec()














# pyinstaller --name 图片播放器 --icon images/window_icon.png --noconsole --add-data images;images main.py
