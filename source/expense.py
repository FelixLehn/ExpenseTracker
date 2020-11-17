from interfaces import Transaction
from viewercategorizer import ViewerCategorizer
from help_functions import add_element_in_db,delete_element_in_db

class Expense(Transaction,ViewerCategorizer):
    def __init__(self):
        super().__init__('expenditures')
        self.loop()

    def loop(self):
        print('Add (A) / Delete (D) / View (V) an expenditures? A/D/V:')
        select=str(input())
        if select.lower() in 'add':
            self.add_element()
        elif select.lower() in 'delete':
            self.delete_element()
        else:
            super().view_loop()
    
    def add_element(self):
        print('Enter your Expense(-)/Income(+) in following format in following format: category/amount/description')
        print('Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other')

        add='y'
        while add.lower() in ['yes','y']:
            try:
                category,amount,description= input().split('/')
                if category and amount and description:  
                    add_element_in_db('expenditures',category,amount,description)
                    print('Do you want to add more?')
                    add=str(input()) 
            except Exception:
                print('Your format was NOT correct. Try again (y) or quit (q)!')
                add=str(input())    
    def delete_element(self):
        print('Delete your Expenditures/Income in following format (Type a category): category/description/month/year :')
        print('Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other')

        delete='y'
        while delete in ['yes','y']:
            try:
                category,description,month, year=input().split('/')
                if category and month and year:  
                    delete_element_in_db('expenditures',category,description,month,year)
                    print('Do you want to delete more?')
                    delete=str(input())
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                delete=str(input()) 
    
