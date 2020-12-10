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
        if select.lower() in 'a':
            self.add_element()
        elif select.lower() in 'de':
            self.delete_element()
        else:
            super().view_loop()
    
    def add_element(self):
        print('Enter your Expense(-)/Income(+) in following format in following format: category/amount/message')
        print('Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other')

        add='y'
        while add.lower() in ['yes','y']:
            try:
                inputs= input().split('/')
                if len(inputs)==3:  
                    add_element_in_db('expenditures',category=inputs[0],amount=inputs[1],message=inputs[2])
                    print('Do you want to add more?')
                    add=str(input()) 
                else: 
                    raise Exception
            except Exception:
                print('Your format was NOT correct. Try again (y) or quit (q)!')
                add=str(input())    
    def delete_element(self):
        print('Delete your Expenditures/Income in following format (Type a category): category/amount/month/year :')
        print('Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other')

        delete='y'
        while delete in ['yes','y']:
            try:
                inputs=input().split('/')
                if len(inputs)==4:  
                    delete_element_in_db('expenditures',category=inputs[0],amount=inputs[1],month=inputs[2],year=inputs[3])
                    print('Do you want to delete more?')
                    delete=str(input())
                else: 
                    raise Exception
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                delete=str(input()) 
    
