from viewer import View
from help_functions import questioner

class ViewerCategorizer(View):
    def __init__(self,membership=''):
        self.membership=membership

    def view_loop(self):
        if self.membership:
            select=questioner('View the whole {} (A) / View a Barchart (B) ?'.format(self.membership),input_needed=True)
            if select.lower() in 'a':
                super().view_results(self.membership)
            elif select.lower() in 'b':
                super().view_barchart(self.membership)
        else :
            try:
                print('View the whole Budget and expense Comparison')
                super().view_budget_to_expense()
            except Exception:
                print('There is nothing to plot :( Insert some values first ;)')
    
