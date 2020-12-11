from budget import Budget
from expense import Expense
from viewercategorizer import ViewerCategorizer
from help_functions import questioner


class Controller():
    def __init__(self):
        self.build_pipeline()
    
    def build_pipeline(self):
        b_or_e=''
        while b_or_e.lower()!='q':
            b_or_e=questioner('Create/Delete/View a Budget (press B) | Add/Delete/View an Expenditure (Press E) | view everything(Press V) | Quit (Press Q)?',input_needed=True)
            if b_or_e.lower() == 'b':
                Budget()
            elif b_or_e.lower() == 'e':
                Expense()
            elif b_or_e.lower() == 'v':
                ViewerCategorizer().view_loop()
def main():
    questioner('Hello there! Please enter your informations so that I am able to help you','What do you want to do? ',input_needed=False)
    Controller()

   

if __name__ == "__main__":
    main()



