# 1. Set up a simple working program
import sqlite3 as db 
import datetime

def expense_db(category=None):
    '''
    Creates a new or connects to exisiting expense database 
    to store the expenditures
    '''
    conn=db.connect('expense.db')
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE expenses(category STRING, amount NUMBER, message STRING, date STRING)'''
    query_select_db='''
    SELECT * FROM expenses WHERE category=?'''
    query_select_all='''
    SELECT * FROM expenses'''
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='expenses' ''')
    if cur.fetchone()[0] < 1:
        cur.execute(query_create_db)
    else:
        if category:
            cur.execute(query_select_db,category)
        else: 
            cur.execute(query_select_all)
    conn.commit()
    results=cur.fetchall()
    conn.close()
    return results

def add_element(category, amount, message=""):
    '''
    adds expenditures in the database
    '''
    date=str(datetime.datetime.now())
    conn=db.connect("expense.db")
    cur=conn.cursor()
    query='''INSERT INTO expenses VALUES (?,?,?,?)'''
    cur.execute(query,(category,amount,message,date))
    conn.commit()
    conn.close()

def delete_element(category, amount, message=""):
    '''
    deletes expenditures in the database
    '''
    conn=db.connect("expensey.db")
    cur=conn.cursor()
    query='''
        DELETE FROM expenses WHERE category='{category} AND message='{message}' 
    '''
    try:
        cur.execute(query) 
        conn.commit()
    except Exception as e: 
        print(e)
    conn.close()
print('Hello there! Please enter your informations so that I am able to help you')
print('Enter your expenditures with an minus (-x) and your incomes with just the number (x)')
print('Do you want to add or delete something? yes (y) : no (n):')
add=str(input())
if add in ['yes','y']:
    print('Enter everything in this format "category:amount:description" and press Enter')
    while add in ['yes','y']:
        category,amount,description= input().split(':')
        add_element(category,amount,description)
        print('Do you want to add more?')
        add=str(input())
print('Do you want to delete something?')
delete=str(input())
if delete in ['yes','y']:
    print('Enter everything in this format "category:amount:description" and press Enter')
    while delete in ['yes','y']:
        category,amount,description=input().split(':')
        delete_element(category,amount,description)
        print('Do you want to delete more?')
        delete=str(input())
print('Do you want to see your expenses?')
view=str(input())
if view in ['yes','y']:
    results= expense_db()
    for entry in results:
        print(('   |   '.join([str(e) for e in entry])))

