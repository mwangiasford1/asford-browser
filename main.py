import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from browser.window import BrowserWindow
from browser.splash import SplashScreen

app = QApplication(sys.argv)
splash = SplashScreen()

def show_main_window():
    splash.close()
    window = BrowserWindow()
    window.show()
    app.window = window

QTimer.singleShot(2000, show_main_window)
sys.exit(app.exec_())