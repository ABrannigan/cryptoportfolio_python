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
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

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
               print(delcurrency + ' has been removed from portfilio')
               file.to_csv('portfolio.csv', index = False)
               print(pd.read_csv('portfolio.csv'))
               
               
def viewfolio():
        '''this function accesses coinmarket cap api 
            and displays current market info related to user portfolio'''
           
        listingsURI = 'https://api.coinmarketcap.com/v2/listings/?convert=USD'
        
        api = {
            
            'X-CMC_PRO_API_KEY': 'c1aa9072-eedf-48a3-8e7d-f5fe74a457b8'
            
        }
        
        request = requests.get(listingsURI , headers=api)
        result = request.json() 
        #data = pd.DataFrame(result['data'])
        data = result['data']
       
        ticker_url_pairs = {}
        for x in data:
            symbol = x['symbol']
            url = x['id']
            ticker_url_pairs[symbol] = url
    
        
        file = pd.read_csv('portfolio.csv' ) #skiprows=1
        #print(file)
        file.columns = map(str.upper, file.columns)
        
        total_value = 0.00
        #price = 0.00
        table = PrettyTable(['Crypto', 'Amount Owned', 'USD' + ' Value', 'Price'])
   
        for i, row in file.iterrows():
            ticker = row['CURRENCY'] 
            shares = row['SHARES']
        
    
            ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[ticker]) + '/' + '?structure=array&convert=' + 'USD'
            request = requests.get(ticker_url, headers=api)
            result = request.json()
            #print(json.dumps(result, sort_keys = True, indent=4))
            
            key = result['data'][0]
            #rank = currency['rank']
            name = key['name']
            #last_updated = currency['last_updated']
            symbol = key['symbol']
            quotes = key['quotes']['USD']
            price = quotes['price']

            value = round(price * float(shares),2)
            total_value = round(value + total_value,2)
                    
            table.add_row([name + ' (' + symbol + ')', str(shares),'$' +str(value),'$' + str(price)])
                
        print(table)
        print()
        print('Total Portfolio Value: ' +'$' + str(total_value))
        print()
        
   
        
       

while True:
    
    choice = input(' Enter "a" to add crypto to portfolio  \n Enter "r" to remove crypto from portfolio \n Enter "q" to exit :' )
    file = open('portfolio.csv', 'a' )
    
    if choice  == 'r':
       delcrypto()
    
    elif choice == 'v':   
        viewfolio()
        
        
    elif choice == 'a':
        addcrypto()
    
    elif choice  == 'q':
        break
    else:
        print('Please Enter a valid choice ')
        
file.close()
        

    
           