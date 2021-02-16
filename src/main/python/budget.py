import sqlite3 as db 
import datetime
from interfaces import Transaction
from viewercategorizer import ViewerCategorizer
from help_functions import add_element_in_db,delete_element_in_db,questioner,data_db, add_element,delete_element


class Budget(Transaction,ViewerCategorizer):
    def __init__(self):
        super().__init__('budget')
        self.add_amount(0)
        self.add_message('Nothing in here')
    def loop(self):
        """
        Asks for add or deletion of a Budget in a Loop
        """
        select=questioner('Create (C) / Delete (D) / View (V) Budget? C:D:V',input_needed=True)
        if select.lower() in 'create':
            self.add()
        elif select.lower() in 'delete':
            self.delete()
        else:
            super().view_loop()
    def add(self):
        message='Enter your Budget for every month in following format (Type a category or "ALL" for everything): category/amount/message/month/year :','Possible Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other'
        add='yes'
        while add.lower() in 'yes':
            inputs=add_element('budget',message)
            if inputs!="400":
                bud=self.add_category(inputs[0])\
                        .add_amount(inputs[1])\
                        .add_message(inputs[2])\
                        .add_month(inputs[3])\
                        .add_year(inputs[4])
                add_element_in_db('budget',category=bud.category,amount=bud.amount,message=bud.message,month=bud.month,year=bud.year)
                print('ADD:'+self.__str__())
                add=questioner('Do you want to add more?', input_needed=True)
            else: 
                add=questioner('Format was not correct! Do you want to try again?', input_needed=True)
        return "200"
    def delete(self):
        message=['Delete your Budget in following format (Type a category or "ALL" for everything): category/month/year :','Categories are : Transport | Household | Abos | Restaurants | Education | Food | Family | Entertainment | Shopping | Investment | Health | Leisure | Other']
        delete='y'
        while delete.lower() in 'yes':
            inputs=delete_element('budget',message)
            if inputs!="400":
                bud=self.add_category(inputs[0])\
                    .add_month(inputs[1])\
                    .add_year(inputs[2])
                delete_element_in_db('budget',category=bud.category,month=bud.month,year=bud.year)
                print('DELETE:'+self.__str__())
                delete=questioner('Dow you want to delete more?',input_needed=True )
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
        return "{Budget_"+self.category+"=>["+str(self.amount)+","+self.message+" for "+self.month+"."+self.year +"}"
    
    def __add__(self,other):
        if self.month==other.month and self.year==other.year:
            amount=self.amount+other.amount
            return f"The Budget for the {self.category} and {other.category} is {amount}"
        else: 
            return f"You can not add Budgets with different months or years"

    def __sub__(self,other):    
        if self.month==other.month and self.year==other.year:
            amount=self.amount-other.amount
            return f"The Budget for the {self.category} minus the {other.category} is {amount}"
        else: 
            return f"You can not subtract Budgets with different months or years"

        




