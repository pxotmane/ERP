# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from os import path
from accueil import Ui_mWin


class Ui_Login(object):
    def showAcceuil(self):
        self.showAcceuil = QtWidgets.QMainWindow()
        self.ui = Ui_mWin()
        self.ui.setupUi(self.showAcceuil)
        Login.hide()
        self.showAcceuil.show()

    def checkLogin(self):
        print(" Entre clicked")
        self.showAcceuil()

    def checkCancel(self):
        print(" Cancel clicked")

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 271)
        Login.setStyleSheet("background-color: #fff;")

        # LABEL LOGIN NAME
        self.LName = QtWidgets.QLabel(Login)
        self.LName.setGeometry(QtCore.QRect(80, 130, 41, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LName.setFont(font)
        self.LName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LName.setAutoFillBackground(False)
        self.LName.setObjectName("LName")
        # LABEL LOGIN NAME

        # LABEL LOGIN PASSWORD
        self.LPasswd = QtWidgets.QLabel(Login)
        self.LPasswd.setGeometry(QtCore.QRect(20, 170, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LPasswd.setFont(font)
        self.LPasswd.setObjectName("LPasswd")
        # LABEL LOGIN PASSWORD

        # LOGIN NAME TEXTFIELD
        self.LEName = QtWidgets.QLineEdit(Login)
        self.LEName.setGeometry(QtCore.QRect(130, 130, 200, 30))
        self.LEName.setStyleSheet("border: 2px solid #dce4ec;\n"
                                  "color: #34495e;\n"
                                  "text-indent: 1px;\n"
                                  "border-radius: 6px;")
        self.LEName.setText("")
        self.LEName.setObjectName("LEName")
        # LOGIN NAME TEXTFIELD

        # LOGIN PASSWORD TEXTFIELD
        self.LEPass = QtWidgets.QLineEdit(Login)
        self.LEPass.setGeometry(QtCore.QRect(130, 170, 200, 30))
        self.LEPass.setStyleSheet("border: 2px solid #dce4ec;\n"
                                  "color: #34495e;\n"
                                  "text-indent: 1px;\n"
                                  "border-radius: 6px;\n"
                                  "")
        self.LEPass.setObjectName("LEPass")
        # LOGIN PASSWORD TEXTFIELD

        # BUTTON ENTER
        self.Entre = QtWidgets.QPushButton(Login)
        self.Entre.setGeometry(QtCore.QRect(130, 220, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Entre.setFont(font)
        self.Entre.setStyleSheet("border: none;\n"
                                 "background: #3498db;\n"
                                 "color: white;\n"
                                 "font-size: 16.5px;\n"
                                 "text-decoration: none;\n"
                                 "border-radius: 4px;\n"
                                 "")
        self.Entre.setObjectName("Entre")
        self.Entre.clicked.connect(self.showAcceuil)
        # ENTER BUTTON

        # CANCEL BUTTON
        self.Cancel = QtWidgets.QPushButton(Login)
        self.Cancel.setGeometry(QtCore.QRect(250, 220, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("border: none;\n"
                                  "background: #3498db;\n"
                                  "color: white;\n"
                                  "font-size: 16.5px;\n"
                                  "text-decoration: none;\n"
                                  "border-radius: 4px;\n"
                                  "")
        self.Cancel.setObjectName("Cancel")
        self.Cancel.clicked.connect(self.checkCancel)
        # CANCEL BUTTON

        self.label = QtWidgets.QLabel(Login)
        #pixmap = QPixmap(os.path.join(os.getcwd(), 'login-user-icon.png'))
        stpath = path.dirname(path.abspath(path.curdir))
        pixmap = QPixmap(r'{}\images\login-user-icon.png'.format(stpath))
        # resize image un Qlabel
        self.label.setPixmap(pixmap.scaled(60, 60, QtCore.Qt.KeepAspectRatio))
        # centering image in Qlabel
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(150, 40, 151, 71))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Entre.setText(_translate("Login", "Entrer"))
        self.LName.setText(_translate("Login", "Nom: "))
        self.LPasswd.setText(_translate("Login", "Mot de passe: "))
        self.Cancel.setText(_translate("Login", "Annuler"))


# import icons_rc
# import images_rc

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
