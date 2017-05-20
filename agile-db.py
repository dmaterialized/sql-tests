# / agile database - creates a mysql database using sqlite3.
# \
# / version: 0.1
# \ date: 2017.05.12
# / initial: 2017.05.12
# \ TODO:
# / - ensure timestamps are set on creation and never again
# \ - migrate daily notes each day as a cleanup task (is that even needed?)
# / -
# \ -
# / -


import sqlite3, numpy

def create_table():
    conn=sqlite3.connect("agile.db")
    cur=conn.cursor()
    # database schema
    #  - daily, weekly, monthly, quarterly lists
    #  - each task is on one list only
    #  - results of each list can be printed out at any time
    #  - why use a database at all? because each item can have metadata.
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (item TEXT, list TEXT, note TEXT, priority INTEGER)")
    # TODO: ensure that timestamp works this way (it may not)
    # TODO: the timestamp needs to be set here but only be passed upon creation.
    # sql code goes in the brackets, always in quotes.
    # Pass code as a string to Execute method of cursor.
    # The above creates a table named store with four columns.
    # the if not exists is to ensure that it can handle being already present.
    conn.commit() # save those changes to the database
    conn.close() # close connection

def add(item,list,note,priority):
    conn=sqlite3.connect("agile.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO tasks VALUES (?,?,?,?)",(item,list,note,priority))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("agile.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM tasks") # select all from tasks.
    rows=cur.fetchall() # store fetch in a variable called rows
    conn.close()
    return rows # will print as a list

def delete(item):
    conn=sqlite3.connect("agile.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM tasks where item=?",(item,)) #should it be item instead?
    conn.commit()
    conn.close()

create_table()
delete('an item')
add('an item', 'daily', 'na', 3)

print("hello")
print(view())
