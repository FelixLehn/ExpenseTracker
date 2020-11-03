import sqlite3 as db 
import datetime
from interfaces import Transaction
from help_functions import add_element_in_db,delete_element_in_db


class Budget(Transaction):
    def __init__(self):
        self.budget_loop()

    def budget_loop(self):
        """
        Asks for add or deletion of a Budget in a Loop
        """
        print('Create or Delete Budget? C:D')
        c_or_d=str(input())
        if c_or_d.lower() in 'create':
            self.add_element()
        else:
            self.delete_element()

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
                print('Your format was NOT correct. Try again!')
                add='yes'    
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
                print('Your format was NOT correct. Try again!')
                delete='y'
    




