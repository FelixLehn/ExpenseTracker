import sqlite3 as db 
import datetime
import dateutil.parser as parser

def add_element_in_db(*args,**kwargs):
    '''
    adds expenditures/budgets in the database

    Input: 
    membership -> budget or expenses
    period -> month or year
    '''

    date=datetime.date.today()
    year,month=(date.year,date.month) if len(kwargs.values())<5 else (kwargs['year'],kwargs['month'])
    date=parser.parse(str(date.day)+'-'+month+'-'+year,dayfirst=True) 
    conn=db.connect("expense.db")
    cur=conn.cursor()
    query_create_db='''
    CREATE TABLE '{}' (category STRING, amount NUMBER, message STRING, date STRING,month STRING,year NUMBER )'''.format(args[0])
    query='''INSERT INTO '{}' VALUES (?,?,?,?,?,?)'''.format(args[0])
    cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(args[0]))
    if cur.fetchone()[0] < 1:
        cur.execute(query_create_db)
        cur.execute(query,(kwargs['category'].lower(),kwargs['amount'],kwargs['message'],date,date.month,date.year))

    else:
        cur.execute(query,(kwargs['category'].lower(),kwargs['amount'],kwargs['message'],date,date.month,date.year))
    conn.commit()
    conn.close()

def delete_element_in_db(*args,**kwargs):
    '''
    deletes expenditures/budgets in the database
    '''
    conn=db.connect("expense.db")
    cur=conn.cursor()
    date=parser.parse('01-'+kwargs['month']+'-'+kwargs['year'],dayfirst=True)  
    query_create_db='''
    CREATE TABLE '{}' (category STRING, amount NUMBER, message STRING, date STRING,month STRING, year NUMBER)'''.format(args[0])
    if args[0]=='budget':
        query='''
            DELETE FROM '{}' WHERE category='{}' AND month='{}' AND year='{}'
        '''.format(args[0],kwargs['category'].lower(), date.month,date.year)
    else:
        query='''
            DELETE FROM '{}' WHERE category='{}' AND amount={} AND month='{}' AND year='{}'
        '''.format(args[0],kwargs['category'].lower(),kwargs['amount'], date.month,date.year)
    try:
        cur.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(args[0]))
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
    CREATE TABLE '{}'(category STRING, amount NUMBER, message STRING, date STRING,month STRING,year STRING )'''.format(membership)
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

def questioner(*args,input_needed=False):
    print(*args,sep="\n")
    if input_needed:
        return str(input())
    return "500"

