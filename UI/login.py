# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 271)
        Login.setMaximumSize(QtCore.QSize(400, 271))
        Login.setStyleSheet("background-color: #fff;")
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
        self.LPasswd = QtWidgets.QLabel(Login)
        self.LPasswd.setGeometry(QtCore.QRect(20, 170, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LPasswd.setFont(font)
        self.LPasswd.setObjectName("LPasswd")
        self.LEName = QtWidgets.QLineEdit(Login)
        self.LEName.setGeometry(QtCore.QRect(130, 130, 200, 30))
        self.LEName.setStyleSheet("border: 2px solid #dce4ec;\n"
                                  "color: #34495e;\n"
                                  "text-indent: 1px;\n"
                                  "border-radius: 6px;")
        self.LEName.setText("")
        self.LEName.setPlaceholderText("")
        self.LEName.setObjectName("LEName")
        self.LEPass = QtWidgets.QLineEdit(Login)
        self.LEPass.setGeometry(QtCore.QRect(130, 170, 200, 30))
        self.LEPass.setStyleSheet("border: 2px solid #dce4ec;\n"
                                  "color: #34495e;\n"
                                  "text-indent: 1px;\n"
                                  "border-radius: 6px;\n"
                                  "")
        self.LEPass.setObjectName("LEPass")
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
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(150, 40, 151, 71))
        self.label.setStyleSheet("image: url(:/login/login-user-icon.png);")
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
from ERP.images import images

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
