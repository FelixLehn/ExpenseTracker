import sqlite3 as db 
import datetime
from transactions import add_element,delete_element

def budget_creator():
    print('Create or Delete Budget? yes:no?')
    c_or_d=str(input())
    if c_or_d.lower() in 'yes':
        add_element('budget')
    else:
        delete_element('budget')



def connect_db(membership,category=None):
    '''
    Creates a new or connects to exisiting expense database 
    to store the expenditures
    '''
    if membership=='e':
        membership='expenditures'
    else:
        membership='budget'
    conn=db.connect('expense.db')
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}'(category STRING, amount NUMBER, message STRING, date STRING,period STRING )'''.format(membership)
    query_select_db='''
    SELECT * FROM '{}' WHERE category=?'''.format(membership)
    query_select_all='''
    SELECT * FROM '{}' '''.format(membership)
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(membership))
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
