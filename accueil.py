# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMainWindow
from os import path


class Ui_mWin(object):
    def setupUi(self, mWin):
        mWin.setObjectName("mWin")
        mWin.setWindowState(QtCore.Qt.WindowMaximized)
        #mWin.resize(1034, 600)
        #mWin.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        mWin.setFont(font)
        icon = QtGui.QIcon()
        stpath = path.abspath(path.curdir)
        icon.addPixmap(QtGui.QPixmap(r'{}\images\logo.png'.format(stpath)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mWin)
        self.centralwidget.setObjectName("centralwidget")
        mWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuVentes = QtWidgets.QMenu(self.menubar)
        self.menuVentes.setObjectName("menuVentes")
        mWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mWin)
        self.statusbar.setObjectName("statusbar")
        mWin.setStatusBar(self.statusbar)
        self.actionClients = QtWidgets.QAction(mWin)
        self.actionClients.setObjectName("actionClients")
        self.actionFournisseurs = QtWidgets.QAction(mWin)
        self.actionFournisseurs.setObjectName("actionFournisseurs")
        self.actionTransporteurs = QtWidgets.QAction(mWin)
        self.actionTransporteurs.setObjectName("actionTransporteurs")
        self.actionAricles = QtWidgets.QAction(mWin)
        self.actionAricles.setObjectName("actionAricles")
        self.actionFamilles = QtWidgets.QAction(mWin)
        self.actionFamilles.setObjectName("actionFamilles")
        self.actionUnit_s = QtWidgets.QAction(mWin)
        self.actionUnit_s.setObjectName("actionUnit_s")
        self.actionNature_op_ration_caisse = QtWidgets.QAction(mWin)
        self.actionNature_op_ration_caisse.setObjectName("actionNature_op_ration_caisse")
        self.actionCodification = QtWidgets.QAction(mWin)
        self.actionCodification.setObjectName("actionCodification")
        self.actionSauvgarder_et_quitter = QtWidgets.QAction(mWin)
        self.actionSauvgarder_et_quitter.setObjectName("actionSauvgarder_et_quitter")
        self.actionQuitter = QtWidgets.QAction(mWin)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFichier.addAction(self.actionClients)
        self.menuFichier.addAction(self.actionFournisseurs)
        self.menuFichier.addAction(self.actionTransporteurs)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionAricles)
        self.menuFichier.addAction(self.actionFamilles)
        self.menuFichier.addAction(self.actionUnit_s)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionNature_op_ration_caisse)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionCodification)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionSauvgarder_et_quitter)
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuVentes.menuAction())

        self.retranslateUi(mWin)
        QtCore.QMetaObject.connectSlotsByName(mWin)

    def retranslateUi(self, mWin):
        _translate = QtCore.QCoreApplication.translate
        mWin.setWindowTitle(_translate("mWin", "IJADA ERP"))
        self.menuFichier.setTitle(_translate("mWin", "Fichier"))
        self.menuVentes.setTitle(_translate("mWin", "Ventes"))
        self.actionClients.setText(_translate("mWin", "Clients"))
        self.actionFournisseurs.setText(_translate("mWin", "Fournisseurs"))
        self.actionTransporteurs.setText(_translate("mWin", "Transporteurs"))
        self.actionAricles.setText(_translate("mWin", "Aricles"))
        self.actionFamilles.setText(_translate("mWin", "Familles"))
        self.actionUnit_s.setText(_translate("mWin", "Unités"))
        self.actionNature_op_ration_caisse.setText(_translate("mWin", "Nature opération caisse "))
        self.actionCodification.setText(_translate("mWin", "Codification"))
        self.actionSauvgarder_et_quitter.setText(_translate("mWin", "Sauvgarder et quitter"))
        self.actionQuitter.setText(_translate("mWin", "Quitter"))

#import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mWin = QtWidgets.QMainWindow()
    ui = Ui_mWin()
    ui.setupUi(mWin)
    mWin.show()
    sys.exit(app.exec_())
