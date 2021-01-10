import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.getcwd() +"//src//main//python")
from expense import Expense

class ExpenseTest(unittest.TestCase):

    @patch('builtins.input',return_value='Transport/10/For the Bus')
    def test_add(self,mock):
        exp=Expense()
        self.assertEqual(exp.add(),"200")
    @patch('builtins.input',return_value='Transport//For the Bus')
    def test_add_2(self,mock):
        exp=Expense()
        self.assertEqual(exp.add(),"200")
    @patch('builtins.input',return_value='Transport/10/')
    def test_add_3(self,mock):
        exp=Expense()
        self.assertEqual(exp.add(),"200")
    @patch('builtins.input',return_value='Transport/For the Bus')
    def test_add_4(self,mock):
        exp=Expense()
        self.assertEqual(exp.add(),"200")
    
    @patch('builtins.input',return_value='Transport/100/July/2020')
    def test_delete_1(self,mock):
        exp=Expense()
        self.assertEqual(exp.delete(),"200")
    @patch('builtins.input',return_value='Transport//July/2020')
    def test_delete_2(self,mock):
        exp=Expense()
        self.assertEqual(exp.delete(),"200")

if __name__ == "__main__": 
    unittest.main()
