# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:48:25 2018

@author: adam
"""
import csv
import os 

def addcrypto():
   
        file = open('portfolio.csv', 'a' )
        fields =['Currency','Shares']
        writer = csv.DictWriter(file, fieldnames = fields, lineterminator = '\n')
        
        file_is_empty = os.stat('portfolio.csv').st_size == 0
       
        if file_is_empty:
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





while True:
    choice = input(' Enter "c" create a new portfolio  \n Enter "e" to edit and existing portfolio \n Enter "q" to exit :' )

    if choice  == 'c':
       file = open('portfolio.csv', 'x')#either change to allow call the file any name or try catch method
       file.close()
       addcrypto()
       
       
    elif choice == 'e':
        addcrypto()
    
    elif choice  == 'q':
        break
    else:
        print('Please Enter a valid choice ')
        

    
           