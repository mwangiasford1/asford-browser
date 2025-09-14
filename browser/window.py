from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import os

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asford Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        # Set window icon
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icons', 'asford.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Create web view
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.google.com"))
        
        # Set central widget
        self.setCentralWidget(self.web_view)