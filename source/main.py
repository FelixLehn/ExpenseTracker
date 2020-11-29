from budget import Budget
from expense import Expense
from viewercategorizer import ViewerCategorizer


class Controller():
    def __init__(self):
        self.build_pipeline()
    
    def build_pipeline(self):
        b_or_e=''
        while b_or_e.lower()!='q':
            print('Create/Delete/View a Budget (press B) | Add/Delete/View an Expenditure (Press E) | view everything(Press V) | Quit (Press Q)?')
            b_or_e=str(input())
            if b_or_e.lower() == 'b':
                Budget()
            elif b_or_e.lower() == 'e':
                Expense()
            elif b_or_e.lower() == 'v':
                ViewerCategorizer().view_loop()
def main():
    print('Hello there! Please enter your informations so that I am able to help you')
    print('What do you want to do? ' )
    control_sequence=Controller()

   

if __name__ == "__main__":
    main()



