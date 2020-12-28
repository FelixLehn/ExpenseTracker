import unittest
from source.viewer import view_results,view_barchart, view_budget_to_expense

class ViewerTest(unittest.TestCase):

    def testresults(self):
        self.assertEqual(view_results("expenditures"), "200")
        self.assertEqual(view_results("budget"), "200")
        self.assertEqual(view_results("nothing"), "200")
        self.assertEqual(view_results(""), "200")
    def testbarchart(self):
        self.assertEqual(view_barchart("expenditures",month="July"),"200")
        self.assertEqual(view_barchart("budget",category="Food"),"200")
        self.assertEqual(view_barchart("expenditures",month=""),"200")
        self.assertEqual(view_barchart("expenditures",category=""),"200")
        self.assertEqual(view_barchart("expenditures",nothing="July"),"404")
        self.assertEqual(view_barchart("",month="July"),"404")
        self.assertEqual(view_barchart(month="July"),"404")
        self.assertEqual(view_barchart("budget"),"200")
    def testviewb_to_e(self):
        
        self.assertEqual(view_budget_to_expense(),"200")
        


if __name__ == "__main__": 
    unittest.main()
