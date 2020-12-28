from help_functions import data_db
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dateutil.parser as parser

class View():
    def __init__(self):
        pass
    
    def view_results(self,membership):
        results= data_db(membership)
        for entry in results:
            print(('\t|\t'.join([str(e) for e in entry])))
        return "200"
    
    def view_barchart(self,*args,**kwargs):
        if kwargs.keys():
            if list(kwargs.keys())[0]=='month':
                date=parser.parse('01'+'-'+kwargs['month']+'-'+'2020',dayfirst=True) 
                query='''SELECT category, sum(amount)
                    FROM {0}
                    WHERE month={1}
                    GROUP BY category 
                    ORDER BY sum(amount) DESC
                    '''.format(args[0],date.month)
            else:
                query='''SELECT category, sum(amount)
                    FROM {0}
                    WHERE category='{1}'
                    GROUP BY month 
                    ORDER BY sum(amount) DESC
                    '''.format(args[0],kwargs['category'])

        
        else:
            query='''SELECT category, sum(amount)
                FROM {0}
                GROUP BY category 
                ORDER BY sum(amount) DESC
                '''.format(args[0])
        category,amount=list(zip(*data_db(args[0],query)))
        y_pos = np.arange(len(category))

        plt.bar(y_pos, amount, align='center', alpha=0.5)
        plt.xticks(y_pos, category)
        plt.ylabel('Total amount')
        plt.title('Budget in a month')
        plt.show()
        return "200"

    def view_budget_to_expense(self):
        query_budget='''SELECT category, sum(amount)
                FROM budget
                GROUP BY category 
                ORDER BY sum(amount) DESC
                '''
        query_expense='''SELECT category, sum(amount)
                FROM expenditures
                GROUP BY category 
                ORDER BY sum(amount) DESC
                '''
        budget=pd.DataFrame(data_db('budget',query_budget),columns=['category','budget'])
        expense=pd.DataFrame(data_db('expenditures',query_expense),columns=['category','expense'])
        expense['expense']=expense['expense'].abs()
        category_amount_matrix=pd.merge(budget,expense,on='category', how='outer').fillna(value=0)
        category_amount_matrix.plot.bar(x='category',y=['budget','expense'])
        plt.show()
        return "200"

