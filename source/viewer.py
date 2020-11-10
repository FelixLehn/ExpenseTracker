from help_functions import data_db
import matplotlib.pyplot as plt
import numpy as np

class View():
    def __init__(self):
        pass
    
    def view_results(self,membership):
        results= data_db(membership)
        for entry in results:
            print(('\t|\t'.join([str(e) for e in entry])))
    
    def view_barchart(self,membership,month="",year=""):
        query='''SELECT category, sum(amount)
                FROM {0}
                GROUP BY category 
                ORDER BY sum(amount) DESC
                '''.format(membership)
        category,amount=list(zip(*data_db(membership,query)))
        y_pos = np.arange(len(category))

        plt.bar(y_pos, amount, align='center', alpha=0.5)
        plt.xticks(y_pos, category)
        plt.ylabel('Total amount')
        plt.title('Budget in a month')
        plt.show()
