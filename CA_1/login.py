# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\adam\Desktop\college\L8 Cert IT Sligo\Secure Software Developement\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cryptoportfolio
import register
from register import *

Reg_Logic = register.Reg_Logic()

class Ui_Login_Dialog(object):
    
    #reg = register.Reg_Logic()
    
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(285, 134)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Login_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Login_Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setInputMask("")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.newUser_btn = QtWidgets.QPushButton(self.groupBox)
        self.newUser_btn.setObjectName("newUser_btn")
        self.horizontalLayout_4.addWidget(self.newUser_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)
        
        self.newUser_btn.clicked.connect(Reg_Logic.regView)

        
    
    
    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "TPayne\'s User Login"))
        self.groupBox.setTitle(_translate("Login_Dialog", "Super Ham!"))
        self.label.setText(_translate("Login_Dialog", "Username"))
        self.label_2.setText(_translate("Login_Dialog", "Password"))
        self.newUser_btn.setText(_translate("Login_Dialog", "New User"))
        self.login_btn.setText(_translate("Login_Dialog", "Login"))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Dialog = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui.setupUi(Login_Dialog)
    Login_Dialog.show()
    sys.exit(app.exec_())'''

