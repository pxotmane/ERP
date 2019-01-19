from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login import Ui_Login
from os import path


"""def showAcceuil(self):
    self.showAcceuil = QtWidgets.QMainWindow()
    self.ui = Ui_Login()
    self.ui.setupUi(self.showAcceuil)
    # Login.hide()
    self.showAcceuil.show()"""


class Form(Ui_Login):
    def __init__(self):
        super(Form, self).__init__()
        self.showAcceuil()
        """self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')"""

    def showAcceuil(self):
        self.showAcceuil = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.showAcceuil)
        # Login.hide()
        self.showAcceuil.show()


if __name__ == "__main__":
    import sys
    import time

    app = QApplication(sys.argv)

    start = time.time()
    stpath = path.abspath(path.curdir)
    splash_pix = QPixmap(r'{}\images\splashscreen1.jpg'.format(stpath))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    while time.time() - start < 2:
        time.sleep(0.001)
        # Form.showAcceuil(self)
        # app.processEvents()

    form = Form()
    # form.show()
    splash.finish(form)
    app.exec_()
