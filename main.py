import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('◁', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        #foward button

        forward_btn = QAction('▷', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        #Refresh button

        reload_btn = QAction('⟲', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

        #Search Box

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url )
        navbar.addWidget(self.url_bar)

app = QApplication(sys.argv)
QApplication.setApplicationName('Ztron Power Search')
window = MainWindow()
app.exec()


