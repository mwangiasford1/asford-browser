from PyQt5.QtWidgets import QSplashScreen, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class SplashScreen(QSplashScreen):
    def __init__(self):
        logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icons', 'logo.jpg')
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path).scaled(400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        else:
            # Create a simple colored rectangle as fallback
            pixmap = QPixmap(400, 300)
            pixmap.fill(Qt.blue)
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.show()