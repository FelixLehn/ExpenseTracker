from interfaces import Transaction
from viewercategorizer import ViewerCategorizer
from help_functions import add_element_in_db,delete_element_in_db,questioner,add_element,delete_element
import datetime

class Expense(Transaction,ViewerCategorizer):
    def __init__(self):
        super().__init__('expenditures')
        date=datetime.date.today()
        self.add_month(date.month)
        self.add_year(date.year)
        self.add_message("Nothing in here")

    def loop(self):
        select=questioner('Add (A) / Delete (D) / View (V) an expenditures? A/D/V:',input_needed=True)
        if select.lower() in 'a':
            self.add()
        elif select.lower() in 'de':
            self.delete()
        else:
            super().view_loop()
    
    def add(self):
        message=['Enter your Expense(-)/Income(+) in following format in following format: category/amount/message','Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other']
        add='yes'
        while add.lower() in ['yes']:
            inputs=add_element('expenditures',message)
            if inputs!="400":
                exp=self.add_category(inputs[0])\
                        .add_amount(inputs[1])\
                        .add_message(inputs[2])
                add_element_in_db('expenditures',category=exp.category,amount=exp.amount,message=exp.message)
                print('ADD:'+self.__str__())
                add=questioner('Do you want to add more?', input_needed=True)
            else: 
                add=questioner('Format was not correct! Do you want to try again?', input_needed=True)
        return "200"
        
    def delete(self):
        message=['Delete your Expenditures/Income in following format (Type a category): category/amount/month/year :','Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other']
        delete='y'
        while delete in ['yes','y']:
            inputs=delete_element('expenditures',message)
            if inputs!="400":
                exp=self.add_category(inputs[0])\
                    .add_amount(inputs[1])\
                    .add_month(inputs[2])\
                    .add_year(inputs[3])
                delete_element_in_db('expenditures',category=exp.category,amount=exp.amount,month=exp.month,year=exp.year)
                print('DELETE:'+self.__str__())                
                delete=questioner('Do you want to delete more?',input_needed=True)
            else: 
                delete=questioner('Format was not correct! Do you want to try again?', input_needed=True)
        return "200"

    def add_category(self,category):
        self.category=category
        return self
    
    def add_amount(self,amount):
        self.amount=int(amount)
        return self

    def add_month(self,month):
        self.month=str(month)
        return self

    def add_year(self,year):
        self.year=str(year)
        return self 

    def add_message(self,message):
        self.message=message
        return self

    def __str__(self):
        return "{Expense_"+self.category+"=>["+str(self.amount)+","+self.message+" for "+self.month+"."+self.year +"}"
    
