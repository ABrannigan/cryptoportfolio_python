# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:48:25 2018

@author: adam
"""
import csv
import os 
#import Pyqt5 
import pandas as pd
import matplotlib.pyplot as plt

#pyuic path script coverts ui to py  C:\ProgramData\Anaconda3\Scripts
# command to run pyuic5 -x "C:\Users\adam\Desktop\test.ui" -o "C:\Users\adam\Desktop\test.py"

def addcrypto():
    '''this  function adds crypto currency to 
        the portfolio csv file fromn user input'''
    
    #file = open('portfolio.csv', 'a' )
    fields =['Currency','Shares']
    writer = csv.DictWriter(file, fieldnames = fields, lineterminator = '\n')
    
    file_empty = os.stat('portfolio.csv').st_size == 0 #check if file is empty
   
    if file_empty:
       writer.writeheader()
   
    while True:
        currency = input('Please Enter currency IE(btc) or enter "q" to exit : ')
        if currency == 'q':
            break
        amount =  input('Please enter amount enter "q" to exit : ')
        if amount == 'q':
            break
        writer.writerow({'Currency' :currency,'Shares': amount})
            
    file.close()        
    print(pd.read_csv('portfolio.csv'))    
    

def delcrypto(): 
    '''this function deletes crypto currency from 
        the portfolio csv file fromn user input'''
        
    file_empty = os.stat('portfolio.csv').st_size == 0 #check if file is empty
    if file_empty:
        print('Portfolio is empty please create a portfolio')
   
    else:
        file = pd.read_csv('portfolio.csv')
        while True:
        
            delcurrency = input('Please enter the crypto you want to delete from portfolio')
            if delcurrency =='q':
               break
            else:
               file =file[file.Currency.str.contains(delcurrency) == False]
               print(delcurrency + 'has been removed from portfilio')
               file.to_csv('portfolio.csv', index = False)
               print(pd.read_csv('portfolio.csv'))
                
            



while True:
    
    choice = input(' Enter "a" to add crypto to portfolio  \n Enter "r" to remove crypto from portfolio \n Enter "q" to exit :' )
    file = open('portfolio.csv', 'a' )
    
    if choice  == 'r':
       delcrypto()
       
    elif choice == 'a':
        addcrypto()
    
    elif choice  == 'q':
        break
    else:
        print('Please Enter a valid choice ')
        
file.close()
        

    
           