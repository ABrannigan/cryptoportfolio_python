# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:24:26 2018

@author: adam
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import cryptoportfolio
import register
import pandas as pd
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import atexit
Reg_Logic = register.Reg_Logic()
Cryp_Logic = cryptoportfolio.Cryp_Logic

class Ui_Login_Dialog(object):
    
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
        self.login_btn.clicked.connect(self.login)
        self.cancel_btn.clicked.connect(Login_Dialog.close)

        
    
    
    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "User Login"))
        self.groupBox.setTitle(_translate("Login_Dialog", "Enter Credentials!"))
        self.label.setText(_translate("Login_Dialog", "Username"))
        self.label_2.setText(_translate("Login_Dialog", "Password"))
        self.newUser_btn.setText(_translate("Login_Dialog", "New User"))
        self.login_btn.setText(_translate("Login_Dialog", "Login"))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel"))
        
    def login(self):
        data_pFile = pd.read_csv('Pfile.csv',header='infer')
        data_pFile.columns = ['Salt','Name','Passwords']
        username = self.user_lineEdit.text()
        print(username)
        password = self.password_lineEdit.text()
        print('password= ' + password)
        check = False
    
        for i , row in data_pFile.iterrows():
            salt = row['Salt']
            storedName = row['Name']
            storedPassword = row['Passwords']
            if storedName == username:
                print('storedPassword = '+str(storedPassword))
                print('storedSalt= '+str(salt))
                decrypted_password = Reg_Logic.decrypt(storedPassword, password, salt)
                print('Decrypted password = ' +str(decrypted_password))
                if str(decrypted_password) == str(password):
                    check = True
            
        if check == False:
            QMessageBox.about(None, "Stop", " Incorrect Username and Password !!")        
        else:
            
            Cryp_Logic.cryptoView(self)
            global filenameH 
            filenameH = Log_Logic.hashFnames(username)
            with open(str(filenameH) + '.csv', 'a') as file:
                Cryp_Logic.encryptFile(str(filenameH) + '.csv',delete=True)
            file.close()
            #atexit.register(Cryp_Logic.encryptFile(str(filenameH) + '.csv'))
            #df.loc[(df['column_name'] == some_value) & df['other_column'].isin(some_values)]

class Log_Logic:
    
    #username = UI_Login_dialog.self.user_lineEdit.text()
    def hashFnames(username):
        password = username.encode('utf-8')
        salt = '10'
        salt = salt.encode('utf-8')
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt ,
            iterations=100000,
            backend=default_backend() )
        return base64.urlsafe_b64encode(kdf.derive(password))
    
    
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Dialog = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui.setupUi(Login_Dialog)
    Login_Dialog.show()
    sys.exit(app.exec_())'''

