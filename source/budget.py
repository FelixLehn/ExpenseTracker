import sqlite3 as db 
import datetime
from interfaces import Transaction
from viewercategorizer import ViewerCategorizer
from help_functions import add_element_in_db,delete_element_in_db


class Budget(Transaction,ViewerCategorizer):
    def __init__(self):
        super().__init__('budget')
        self.loop()

    def loop(self):
        """
        Asks for add or deletion of a Budget in a Loop
        """
        print('Create (C) / Delete (D) / View (V) Budget? C:D:V')
        select=str(input())
        if select.lower() in 'create':
            self.add_element()
        elif select.lower() in 'delete':
            self.delete_element()
        else:
            super().view_loop()
    def add_element(self):
        print('Enter your Budget for every month in following format (Type a category or "ALL" for everything): category/amount/message/month/year :')
        print('Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other')
        add='y'
        while add.lower() in ['yes','y']:
            try:
                inputs= input().split('/')
                if len(inputs)==5:  
                    add_element_in_db('budget',category=inputs[0],amount=inputs[1],message=inputs[2],month=inputs[3],year=inputs[4])
                    print('Do you want to add more?')
                    add=str(input()) 
                else: 
                    raise Exception
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                add=str(input()) 

    def delete_element(self):
        print('Delete your Budget in following format (Type a category or "ALL" for everything): category/month/year :')
        print('Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other')
        delete='y'
        while delete in ['yes','y']:
            try:
                inputs=input().split('/')
                if len(inputs)==3:  
                    delete_element_in_db('budget',category=inputs[0],month=inputs[1],year=inputs[2])
                    print('Do you want to delete more?')
                    delete=str(input())
                else: 
                    raise Exception
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                delete=str(input()) 
    
        




