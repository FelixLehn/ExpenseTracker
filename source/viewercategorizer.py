from viewer import View
from help_functions import questioner

class ViewerCategorizer(View):
    def __init__(self,membership=''):
        self.membership=membership

    def view_loop(self):
        if self.membership:
            select=questioner('View the whole {} (A) / monthly basis (B) / Category Basis (C) ?'.format(self.membership),input_needed=True)
            if select.lower() in 'a':
                select=questioner('Table (T) / Barchart (B) ?',input_needed=True)
                if select.lower() in 't':
                    super().view_results(self.membership)
                else: 
                    super().view_barchart(self.membership)
            elif select.lower() in 'b':
                select=questioner('Which month?',input_needed=True)
                super().view_barchart(self.membership,month=select)
            elif select.lower() in 'c':
                select=questioner('Which category do you want to see in your {}'.format(self.membership),input_needed=True)
                super().view_barchart(self.membership,category=select)
        else :
            try:
                print('View the whole Budget and expense Comparison')
                super().view_budget_to_expense()
            except Exception:
                print('There is nothing to plot :( Insert some values first ;)')
    
