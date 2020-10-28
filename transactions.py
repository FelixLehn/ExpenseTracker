import sqlite3 as db 
import datetime

def add_element(membership):
    print('Enter your {} in following format: category/amount/description/month/year'.format(membership))
    add='y'
    while add.lower() in ['yes','y']:
        try:
            category,amount,description,month,year= input().split('/')
            if category and amount and description and month and year:  
                add_element_in_db(membership,category,amount,description,month,year)
                print('Do you want to add more?')
                add=str(input()) 
        except Exception:
            print('Your format was NOT correct. Try again!')
            add='yes'
def delete_element(membership):
    print('Enter your wished delete {} in following format: category/month/year'.format(membership))
    delete='y'
    while delete in ['yes','y']:
        try:
            category,month,year=input().split('/')
            if category and month and year:  
                delete_element_in_db(membership,category,month,year)
                print('Do you want to delete more?')
                delete=str(input())
        except Exception:
            print('Your format was NOT correct. Try again!')
            delete='y'
        
def add_element_in_db(membership:str,category, amount, message="",month="",year=""):
    '''
    adds expenditures/budgets in the database

    Input: 
    membership -> budget or expenses
    period -> month or year
    '''
    date=str(datetime.datetime.now())
    conn=db.connect("expense.db")
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}' (category STRING, amount NUMBER, message STRING, date STRING,month STRING,year NUMBER )'''.format(membership)
    query='''INSERT INTO '{}' VALUES (?,?,?,?,?,?)'''.format(membership)
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(membership))
    if cur.fetchone()[0] < 1:
        cur.execute(query_create_db)
    else:
        cur.execute(query,(category,amount,message,date,month,year))
    conn.commit()
    conn.close()

def delete_element_in_db(membership:str,category,month="",year=""):
    '''
    deletes expenditures/budgets in the database
    '''
    conn=db.connect("expense.db")
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}' (category STRING, amount NUMBER, message STRING, date STRING,month STRING, year NUMBER)'''.format(membership)
    query='''
        DELETE FROM '{}' WHERE category='{}' AND month='{}' AND year='{}'
    '''.format(membership,category, month, year)
    try:
        cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(membership))
        if cur.fetchone()[0] < 1:
            cur.execute(query_create_db)
        else: 
            cur.execute(query) 
        conn.commit()
    except Exception as e: 
        print(e)
    finally: 
        conn.close()

def transaction_creator():
    print('Add or Delete an expenditures:yes/no:')
    a_or_d=str(input())
    if a_or_d.lower() in 'yes':
        add_element('expenditures')
    else:
        delete_element('expenditures')