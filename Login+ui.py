from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("UI/login.ui")
dlg.show()
app.exec()