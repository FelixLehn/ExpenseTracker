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
        print('Enter your Budget for every month in following format (Type a category or "ALL" for everything): category/amount/description :')
        add='y'
        while add.lower() in ['yes','y']:
            try:
                category,amount,description= input().split('/')
                if category and amount and description:  
                    add_element_in_db('budget',category,amount,description)
                    print('Do you want to add more?')
                    add=str(input()) 
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                add=str(input()) 

    def delete_element(self):
        print('Delete your Budget in following format (Type a category or "ALL" for everything): category :')
        delete='y'
        while delete in ['yes','y']:
            try:
                category=input()
                if category:  
                    delete_element_in_db('budget',category)
                    print('Do you want to delete more?')
                    delete=str(input())
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                delete=str(input()) 
    
        




