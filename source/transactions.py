from interfaces import Transaction
from help_functions import add_element_in_db,delete_element_in_db

class Expense(Transaction):
    def __init__(self):
        self.expense_loop()

    def expense_loop(self):
        print('Add or Delete an expenditures? yes/no:')
        a_or_d=str(input())
        if a_or_d.lower() in 'yes':
            self.add_element()
        else:
            self.delete_element()
    
    def add_element(self):
        print('Enter your Expense(-)/Income(+) in following format in following format: category/amount/description')
        add='y'
        while add.lower() in ['yes','y']:
            try:
                category,amount,description= input().split('/')
                if category and amount and description:  
                    add_element_in_db('expenditures',category,amount,description)
                    print('Do you want to add more?')
                    add=str(input()) 
            except Exception:
                print('Your format was NOT correct. Try again!')
                add='yes'    
    def delete_element(self):
        print('Delete your Expenditures/Income in following format (Type a category or "ALL" for everything): category/description/month/year :')
        delete='y'
        while delete in ['yes','y']:
            try:
                category,description,month, year=input().split('/')
                if category and month and year:  
                    delete_element_in_db('expenditures',category,description,month,year)
                    print('Do you want to delete more?')
                    delete=str(input())
            except Exception:
                print('Your format was NOT correct. Try again!')
                delete='y'
    
