# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:24:26 2018

@author: adam
"""
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import os 
#import Pyqt5 
import pandas as pd
import requests
from prettytable import PrettyTable

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 40, 161, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.cryptoAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.cryptoAdd.setGeometry(QtCore.QRect(50, 60, 113, 20))
        self.cryptoAdd.setObjectName("cryptoAdd")
        
        self.amountAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.amountAdd.setGeometry(QtCore.QRect(50, 100, 113, 20))
        self.amountAdd.setObjectName("amountAdd")
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(70, 130, 75, 23))
        self.addButton.setObjectName("addButton")
        
        self.cryptoDel = QtWidgets.QLineEdit(self.centralwidget)
        self.cryptoDel.setGeometry(QtCore.QRect(350, 60, 113, 20))
        self.cryptoDel.setObjectName("cryptoDel")
        
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(360, 90, 91, 21))
        self.delButton.setObjectName("delButton")
        
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(210, 400, 75, 23))
        self.viewButton.setObjectName("viewButton")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 40, 111, 21))
        self.label_3.setObjectName("label_3")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 170, 441, 221))
        self.textBrowser.setObjectName("textBrowser")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # connect functions to buttons
        self.addButton.clicked.connect(self.addcrypto)
        self.delButton.clicked.connect(self.delcrypto)
        self.viewButton.clicked.connect(self.viewfolio)

        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "AddCrypto"))
        self.delButton.setText(_translate("MainWindow", "RemoveCrypto"))
        self.viewButton.setText(_translate("MainWindow", "ViewPortfolio"))
        self.label.setText(_translate("MainWindow", "Enter Crypto eg:(BTC)"))
        self.label_2.setText(_translate("MainWindow", "Amount"))
        self.label_3.setText(_translate("MainWindow", "Enter Crypto eg:(BTC)"))
    
    def addcrypto(self):
        '''this  function adds crypto currency to 
            the portfolio csv file fromn user input'''
    
        file = open('portfolio.csv', 'a' )
        fields =['Currency','Shares']
        writer = csv.DictWriter(file, fieldnames = fields, lineterminator = '\n')
        
        file_empty = os.stat('portfolio.csv').st_size == 0 #check if file is empty
       
        if file_empty:
           writer.writeheader()
       
        currency = self.cryptoAdd.text().upper()
        amount =  self.amountAdd.text()
        self.amountAdd.clear()
        self.cryptoAdd.clear()
        writer.writerow({'Currency' :currency,'Shares': amount})
        QMessageBox.about(None, "Stop", str(amount + ': ' + currency + " has been added to portfiolio !!"))   
        file.close()        

    def delcrypto(self): 
        '''this function deletes crypto currency from 
            the portfolio csv file fromn user input'''
        
        file_empty = os.stat('portfolio.csv').st_size == 0 #check if file is empty
        if file_empty:
            QMessageBox.about(None, "Stop", " Portfolio is empty please create a portfolio !!")   
        else:
            file = pd.read_csv('portfolio.csv')
            delcurrency = self.cryptoDel.text().upper()
            file = file[file.Currency.str.contains(delcurrency) == False]
            print(delcurrency + ' has been removed from portfilio')
            file.to_csv('portfolio.csv', index = False)
            QMessageBox.about(None, "Stop", str(delcurrency + " has been removed from portfolio !!"))       
        self.cryptoDel.clear()   
            
    def viewfolio(self):
        '''this function accesses coinmarket cap api 
            and displays current market info related to user portfolio'''
           
        listings_url = 'https://api.coinmarketcap.com/v2/listings/?convert=USD'
        api = {
            'X-CMC_PRO_API_KEY': 'c1aa9072-eedf-48a3-8e7d-f5fe74a457b8'    
        }
        #api call pass api key to header for authentication
        request = requests.get(listings_url , headers=api)
        result = request.json() 
        data = result['data']
        #save symbol and id in a dictionary 
        ticker_url_pairs = {}
        for x in data:
            symbol = x['symbol']
            url = x['id']
            ticker_url_pairs[symbol] = url
    
        
        file = pd.read_csv('portfolio.csv' ) 
        file.columns = map(str.upper, file.columns)
        
        total_value = 0.00
        #price = 0.00
        table = PrettyTable(['Name','Symbol', 'Amount Owned', 'USD' + ' Value', 'Price'])
   
        for i, row in file.iterrows():
            ticker = row['CURRENCY'] 
            shares = row['SHARES']
        
            ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[ticker]) + '/' + '?structure=array&convert=' + 'USD'
            request = requests.get(ticker_url, headers=api)
            result = request.json()
            key = result['data'][0]
            name = key['name']
            symbol = key['symbol']
            quotes = key['quotes']['USD']
            price = quotes['price']

            value = round(price * float(shares),2)
            total_value = round(value + total_value,2)
                    
            table.add_row([name , '  (' + symbol + ')', str(shares),'$' +str(value),'$' + str(price)])
                
        table.add_row([' ',' ',' ',' ' ,' '])
        table.add_row(['Total Portfolio Value :','$' + str(total_value),' ' , ' ', ' '])
        table_string = table.get_string()
        self.textBrowser.setText(table_string).setFontFamily("monospace")
        
        #print(table)
        #print()
       # print('Total Portfolio Value: ' +'$' + str(total_value))
        #print()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

