import unittest
from unittest.mock import patch, MagicMock
from source.help_functions import questioner

class QuestionerTest(unittest.TestCase):

    def testquestions(self):
        self.assertEqual(questioner("What do you want?",input_needed=False), "500")
        self.assertEqual(questioner("What do you want?",input_needed=True), "500")
        self.assertEqual(questioner(1,3,2,4,input_needed=False), "500")
        self.assertEqual(questioner([1,2,3,4],input_needed=False), "500")
        self.assertEqual(questioner("What is {}".format("it about?"),input_needed=False), "500")

if __name__ == "__main__": 
    unittest.main()
