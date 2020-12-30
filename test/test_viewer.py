import unittest
from unittest.mock import patch 
import sys
import os
sys.path.append(os.getcwd() +"//src")
from src.viewer import View

class ViewerTest(unittest.TestCase):
    def testresults(self):
        v=View()
        self.assertEqual(v.view_results("expenditures"), "200")
        self.assertEqual(v.view_results("budget"), "200")
        self.assertEqual(v.view_results("nothing"), "200")
        self.assertEqual(v.view_results(""), "200")
    def testbarchart(self):
        v=View()
        self.assertEqual(v.view_barchart("expenditures",month="July"),"200")
        self.assertEqual(v.view_barchart("budget",category="Food"),"200")
        self.assertEqual(v.view_barchart("expenditures",month=""),"200")
        self.assertEqual(v.view_barchart("expenditures",category=""),"200")
        self.assertEqual(v.view_barchart("expenditures",nothing="July"),"404")
        self.assertEqual(v.view_barchart("",month="July"),"404")
        self.assertEqual(v.view_barchart(month="July"),"404")
        self.assertEqual(v.view_barchart("budget"),"200")
    def testviewb_to_e(self):
        v=View()
        self.assertEqual(v.view_budget_to_expense(),"200")
        


if __name__ == "__main__": 
    unittest.main()
