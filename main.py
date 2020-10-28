from transactions import transaction_creator,add_element,delete_element
from budget import budget_creator,connect_db

print('Hello there! Please enter your informations so that I am able to help you')
print('What do you want to do? Create/Delete a Budget (press B), Add/Delete an Expenditure (Press E), view your budget/expenses (Press V)?' )
b_or_e=str(input())
if b_or_e.lower() == 'b':
    budget_creator()
elif b_or_e.lower() == 'e':
    transaction_creator()

print('Do you want to see your expenses (press e), your budget (press b) or quit programm (press q):')
view=str(input())
if view != 'q':
    results= connect_db(view)
    for entry in results:
        print(('   |   '.join([str(e) for e in entry])))

