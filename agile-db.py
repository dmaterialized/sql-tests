# / agile database - creates a mysql database using sqlite3.
# \
# / version: 0.1
# \ date: 2017.05.12
# / initial: 2017.05.12
# \ TODO:
# / -
# \ -
# / -
# \ -
# / -


import sqlite3

def create_table:
    conn=sqlite3.connect("agile.db")
    cur=conn.cursor()
    # database schema
    #  - daily, weekly, monthly, quarterly lists
    #  - each task is on one list
    #  - items can have priority
    #
    #

    cur.execute("CREATE TABLE IF NOT EXISTS tasks (item TEXT, list TEXT, note TEXT, order INTEGER)")
    # sql code goes in the brackets, always in quotes.
    # Pass code as a string to Execute method of cursor.
    # The above creates a table named store with four columns.
    # the if not exists is to ensure that it can handle being already present.
    conn.commit() # save those changes to the database
    conn.close() # close connection
