import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.getcwd() +"//src")

from src.help_functions import questioner

class QuestionerTest(unittest.TestCase):

    def testquestions(self):
        self.assertEqual(questioner("What do you want?",input_needed=False), "500")
        self.assertEqual(questioner(1,3,2,4,input_needed=False), "500")
        self.assertEqual(questioner([1,2,3,4],input_needed=False), "500")
        self.assertEqual(questioner("What is {}".format("it about?"),input_needed=False), "500")
    
    @patch("builtins.input",return_value="Nothing")
    def test_input_needed(self,input):
        self.assertEqual(questioner("What do you want?",input_needed=True), "Nothing")

if __name__ == "__main__": 
    unittest.main()
