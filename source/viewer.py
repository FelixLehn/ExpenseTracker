from help_functions import connect_db

class View():
    def __init__(self):
        self.view_loop()
    
    def view_loop(self):
        print('Do you want to see your expenses (press e), your budget (press b):')
        view=str(input())
        results= connect_db(view)
        for entry in results:
            print(('   |   '.join([str(e) for e in entry])))
