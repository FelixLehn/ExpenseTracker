from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def add_element(self,category,amount, description, month,year):
        pass
    @abstractmethod
    def delete_element(self,category,amount, description, month,year):
        pass