from budget import Budget
from expense import Expense
from viewer import View

print('Hello there! Please enter your informations so that I am able to help you')
print('What do you want to do? ' )
b_or_e=''
while b_or_e.lower()!='q':
    print('Create/Delete/View a Budget (press B) | Add/Delete/View an Expenditure (Press E) | view everything(Press V) | Quit (Press Q)?')
    b_or_e=str(input())
    if b_or_e.lower() == 'b':
        Budget()
    elif b_or_e.lower() == 'e':
        Expense()
    elif b_or_e.lower() == 'v':
        View()



