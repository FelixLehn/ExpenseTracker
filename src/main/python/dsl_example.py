from budget import Budget
from expense import Expense

family=Budget()\
    .add_category('family_kids')\
    .add_amount('200')\
    .add_message('The kids are spending our money')\
    .add_month('March')\
    .add_year('2021')

dog=Budget()\
    .add_category('family_dog')\
    .add_amount('100')\
    .add_message('The dog is eating too much')\
    .add_month('March')\
    .add_year('2021')
cat=Budget()\
    .add_category('family_cat')\
    .add_amount('50')\
    .add_message('The cat eats mouses')\
    .add_month('March')\
    .add_year('2021')

diff_cat_dog=dog-cat

print(f'What is going on with our {family}')
print(f'{family + dog}. That is our Budget')
print(f'{family + cat}. Thats much better than a dog! Our Budgets for other stuff is going to be increased by {diff_cat_dog}')

