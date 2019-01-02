# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:24:26 2018

@author: adam
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import re
import cryptoportfolio
import login
import csv
import base64
import binascii
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Ui_Register_Dialog(object):
    
    def setupUi(self, Register_Dialog):
        Register_Dialog.setObjectName("Register_Dialog")
        Register_Dialog.resize(372, 187)
        Register_Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Register_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Register_Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.username_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.confirmPassword_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.confirmPassword_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword_lineEdit.setObjectName("confirmPassword_lineEdit")
        self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)
        
        self.add_btn.clicked.connect(self.addUser)
        self.cancel_btn.clicked.connect(Register_Dialog.close)
        
        
    def retranslateUi(self, Register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register New User"))
        self.groupBox.setTitle(_translate("Register_Dialog", "Please Fill Fields Below"))
        self.label_2.setText(_translate("Register_Dialog", "Username"))
        self.label.setText(_translate("Register_Dialog", "Password"))
        self.label_3.setText(_translate("Register_Dialog", "Confirm Password"))
        self.label_4.setText(_translate("Register_Dialog", "Paswrod must be contain mix of upper/lower case numbers an special chasrs!"))
        self.add_btn.setText(_translate("Register_Dialog", "Add"))
        self.cancel_btn.setText(_translate("Register_Dialog", "Cancel"))
        
        
    def addUser(self):
        pFile = pd.read_csv('Pfile.csv',header='infer')
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        cpassword = self.confirmPassword_lineEdit.text()
        
        if not username:
            QMessageBox.about(None, "Stop", " Username Missing!!")#. setDefaultButton()
        elif username in pFile:
            QMessageBox.about(None, "Stop", " Username Taken !!")
        elif (len(password)<6 or len(password)>12):
            QMessageBox.about(None, "Stop", " Password Must be between 6-12 Chars long")
        elif not re.search("[a-z]",password):
            QMessageBox.about(None, "Stop", " Password Must have lower case letters !!eg( [A-Z])")
        elif not re.search("[0-9]",password):
            QMessageBox.about(None, "Stop", " Password Must have @ least 1 number !! eg([0-9])")
        elif not re.search("[A-Z]",password):
            QMessageBox.about(None, "Stop", " Password Must have  @ least 1 upper case letter !!eg( [A-Z])")
        elif not re.search("[$#@]",password):
            QMessageBox.about(None, "Stop", " Password Must have special char !! eg([$#@])")
        elif password != cpassword:
            QMessageBox.about(None, 'Dang it!', 'Passwords Do Not Match')
        else:
            print(username)
            salt = str(os.urandom(16))
            salt = salt.replace('\\','')
            salt = salt.encode()
            print('Salt before passed= '+str(salt))
            password = Reg_Logic.encrypt(self,password,salt)
            password.decode('utf-8')
            print(password)
            cpassword = None
            f = open('Pfile.csv', 'a')
            fields =['Salt','Name','Passwords']
            writer = csv.DictWriter(f, fieldnames = fields, lineterminator = '\n')
            file_empty = os.stat('pFile.csv').st_size == 0 #check if file is empty
            if file_empty:
               writer.writeheader()
            #salt =binascii.hexlify(salt).decode()
            writer.writerow({'Salt' :salt,'Name': username,'Passwords': password},)
            f.close
            QMessageBox.about(None, 'Awesome!!', 'User Added SUCCESSFULLY!')
    

class Reg_Logic:
    
    #def __init__(self):

    def regView(self):
            self.Register_Dialog = QtWidgets.QDialog()
            self.ui = Ui_Register_Dialog()
            self.ui.setupUi(self.Register_Dialog)
            self.Register_Dialog.show()    
            
    
    def encrypt(self,plaintext,salty):
        password = plaintext.encode('utf-8')
        print('password = '+str(password))
        salt = salty
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt ,
            iterations=100000,
            backend=default_backend() )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        token = f.encrypt(password)
        print('Salt after encrypt= '+str(salt))
        print('Cypher encrypt= '+ str(token))
        return token
    
    def decrypt(self,cypher,plaintext,salty):
        try:
            password = plaintext.encode('utf-8')
            print('password decrypt in= '+str(password))
            cypher = cypher[2:-1]#
            cypher = cypher.encode('utf-8')
            print('cypher decrypt= '+str(cypher))
            salt = salty[2:-1]
            salt = salt.replace('\\','')
            salt = salt.encode()
            print('salt = '+str(salt))
            #salt = salt
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend() )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            #key = base64.urlsafe_b64encode(kdf.derive(password))
            f = Fernet(key)
            token = f.decrypt(cypher)
            print(token)
            return token.decode('utf-8')
        except:
            print('Sorry Invalid Token')
                
        
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register_Dialog = QtWidgets.QDialog()
    ui = Ui_Register_Dialog()
    ui.setupUi(Register_Dialog)
    Register_Dialog.show()
    sys.exit(app.exec_())'''
    
    

