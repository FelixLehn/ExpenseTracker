from abc import ABCMeta, abstractmethod

class Transaction(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'add_element') and 
                callable(subclass.add_element) and 
                hasattr(subclass, 'delete_element') and 
                callable(subclass.delete_element) and
                hasattr(subclass,'loop') and
                callable(subclass.loop) or 
                NotImplemented)

    @abstractmethod
    def add_element(self,category,amount, description, month,year):
        raise NotImplementedError

    @abstractmethod
    def delete_element(self,category,amount, description, month,year):
        raise NotImplementedError

    @abstractmethod
    def loop(self):
        raise NotImplementedError

