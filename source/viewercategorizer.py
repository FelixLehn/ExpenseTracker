from viewer import View

class ViewerCategorizer(View):
    def __init__(self,membership=''):
        self.membership=membership

    def view_loop(self):
        if self.membership:
            print('View the whole {} (A) / View a Barchart (B) ?'.format(self.membership))
            select=str(input())
            if select.lower() in 'a':
                super().view_results(self.membership)
            elif select.lower() in 'b':
                super().view_barchart(self.membership)
        else :
            print('View the whole Budget and expense Comparison')
            super().view_budget_to_expense()

    
