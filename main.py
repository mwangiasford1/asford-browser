import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from browser.window import BrowserWindow
from browser.splash import SplashScreen

app = QApplication(sys.argv)
# Set application icon for taskbar
icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons', 'asford.ico')
if os.path.exists(icon_path):
    from PyQt5.QtGui import QIcon
    app.setWindowIcon(QIcon(icon_path))
splash = SplashScreen()

def show_main_window():
    splash.close()
    window = BrowserWindow()
    window.show()
    app.window = window

QTimer.singleShot(2000, show_main_window)
sys.exit(app.exec_())