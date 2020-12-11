from interfaces import Transaction
from viewercategorizer import ViewerCategorizer
from help_functions import add_element_in_db,delete_element_in_db,questioner

class Expense(Transaction,ViewerCategorizer):
    def __init__(self):
        super().__init__('expenditures')
        self.loop()

    def loop(self):
        select=questioner('Add (A) / Delete (D) / View (V) an expenditures? A/D/V:',input_needed=True)
        if select.lower() in 'a':
            self.add_element()
        elif select.lower() in 'de':
            self.delete_element()
        else:
            super().view_loop()
    
    def add_element(self):
        inputs= questioner('Enter your Expense(-)/Income(+) in following format in following format: category/amount/message','Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other',input_needed=True)

        add='y'
        while add.lower() in ['yes','y']:
            try:
                inputs= inputs.split('/')
                if len(inputs)==3:  
                    add_element_in_db('expenditures',category=inputs[0],amount=inputs[1],message=inputs[2])
                    add=questioner('Do you want to add more?',input_needed=True)
                else: 
                    raise Exception
            except Exception:
                print('Your format was NOT correct. Try again (y) or quit (q)!')
                add=str(input())    
    def delete_element(self):
        inputs=questioner('Delete your Expenditures/Income in following format (Type a category): category/amount/month/year :','Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other',input_needed=True )

        delete='y'
        while delete in ['yes','y']:
            try:
                inputs=inputs.split('/')
                if len(inputs)==4:  
                    delete_element_in_db('expenditures',category=inputs[0],amount=inputs[1],month=inputs[2],year=inputs[3])
                    delete=questioner('Do you want to delete more?',input_needed=True)
                else: 
                    raise Exception
            except Exception:
                print('Your format was NOT correct. Try again (t) or quit (q)!')
                delete=str(input()) 
    
