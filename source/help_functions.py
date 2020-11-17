import sqlite3 as db 
import datetime

def add_element_in_db(membership:str,category, amount, message="",month="",year=""):
    '''
    adds expenditures/budgets in the database

    Input: 
    membership -> budget or expenses
    period -> month or year
    '''
    date=datetime.date.today()
    if not month:
        year,month=date.year,date.month
    conn=db.connect("expense.db")
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}' (category STRING, amount NUMBER, message STRING, date STRING,month STRING,year NUMBER )'''.format(membership)
    query='''INSERT INTO '{}' VALUES (?,?,?,?,?,?)'''.format(membership)
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(membership))
    if cur.fetchone()[0] < 1:
        cur.execute(query_create_db)
        cur.execute(query,(category,amount,message,date,month,year))

    else:
        cur.execute(query,(category,amount,message,date,month,year))
    conn.commit()
    conn.close()

def delete_element_in_db(membership:str,category,description="",month="",year=""):
    '''
    deletes expenditures/budgets in the database
    '''
    conn=db.connect("expense.db")
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}' (category STRING, amount NUMBER, message STRING, date STRING,month STRING, year NUMBER)'''.format(membership)
    query='''
        DELETE FROM '{}' WHERE category='{}' AND message ='{}' AND month='{}' AND year='{}'
    '''.format(membership,category,description, month, year)
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


def data_db(membership,query=None):
    '''
    Creates a new or connects to exisiting expense database 
    to store the expenditures
    '''
    conn=db.connect('expense.db')
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}'(category STRING, amount NUMBER, message STRING, date STRING,period STRING )'''.format(membership)
    query_select_all='''    SELECT * FROM '{}' '''.format(membership)
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(membership))
    if cur.fetchone()[0] < 1:
        cur.execute(query_create_db)
    else:
        if query:
            if isinstance(query,list):
                cur.execute(query[0],*query[1])
            else:
                cur.execute(query)

        else: 
            cur.execute(query_select_all)
    conn.commit()
    results=cur.fetchall()
    conn.close()
    return results