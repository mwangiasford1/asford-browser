from PyQt5.QtWidgets import QSplashScreen, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class SplashScreen(QSplashScreen):
    def __init__(self):
        logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icons', 'logo.jpg')
        pixmap = QPixmap(logo_path).scaled(400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.show()