from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time


class Form(QDialog):
    """ Just a simple dialog with a couple of widgets
    """

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.lineedit = QLineEdit("Write something and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        #self.connect(self.lineedit, SIGNAL("returnPressed()"), self.update_ui)

    def update_ui(self):
        self.browser.append(self.lineedit.text())


if __name__ == "__main__":
    import sys
    import time

    app = QApplication(sys.argv)

    # create splashscreen, use the pic in folder img/bee2.jpg
    splash_pix = QPixmap('img/bee2.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # set the splash window flag, keep the window stay on tophint and frameless
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash.setMask(splash_pix.mask())
    # show the splashscreen
    splash.show()
    # show Message
    splash.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)

    # create elapse timer to cal time
    timer = QtCore.QElapsedTimer()
    timer.start()
    # we give 3 secs
    while timer.elapsed() < 3000:
        app.processEvents()

    # create the main form
    form = Form()
    form.show()
    # call finish method to destory the splashscreen
    splash.finish(form)
    sys.exit(app.exec_())
