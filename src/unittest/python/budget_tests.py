import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.getcwd() +"//src//main//python")
from budget import Budget

class BudgetTest(unittest.TestCase):

    @patch('builtins.input',return_value='Transport/100/For the Bus/October/2020')
    def test_add(self,mock):
        bud=Budget()
        self.assertEqual(bud.add(),"200")
    @patch('builtins.input',return_value='Transport//For the Bus')
    def test_add_2(self,mock):
        bud=Budget()
        self.assertEqual(bud.add(),"200")
    @patch('builtins.input',return_value='Transport/100//October/2020')
    def test_add_3(self,mock):
        bud=Budget()
        self.assertEqual(bud.add(),"200")
    @patch('builtins.input',return_value='Transport/For the Bus')
    def test_add_4(self,mock):
        bud=Budget()
        self.assertEqual(bud.add(),"200")
    
    @patch('builtins.input',return_value='Transport/July/2020')
    def test_delete_1(self,mock):
        bud=Budget()
        self.assertEqual(bud.delete(),"200")
    @patch('builtins.input',return_value='Transport//2020')
    def test_delete_2(self,mock):
        bud=Budget()
        self.assertEqual(bud.delete(),"200")

if __name__ == "__main__": 
    unittest.main()
