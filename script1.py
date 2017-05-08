# / database loader - creates an sql database.
# \
# / version: 0.1
# \ date: 2017.05.07
# / initial: 2017.05.07
# \ TODO:
# / - delete, move, search functions
# \ - visual browser
# / - add items by typing them in
# \
# /



import sqlite3

# going to do this entire thing in a Create function.

def create_table():
    # ====  i n i t    d a t a b a s e  =====================
    # - first create the database
    conn=sqlite3.connect("lite.db") # establish connection

    # - create the cursor object - this has been moved to the insert func
    # cur=conn.cursor()
    # create the table
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # sql code goes in the brackets, always in quotes.
    # Pass code as a string to Execute method of cursor.
    # The above creates a table named store with four columns.
    # the if not exists is to ensure that it can handle being already present.
    conn.commit() # save those changes to the database
    conn.close() # close connection

def insert(item,quantity,price): # ensure that you set the arguments
    conn=sqlite3.connect("lite.db")

    # - create the cursor object -
    cur=conn.cursor()
    # insert some values (records) into the columns
    # old version:
    #cur.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    # always list in the same order that the columns were defined as.
    # new version using variables "?":
    # first list the ???, then, after the SQL code, identify variables
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit() # save those changes to the database
    conn.close() # close connection

# ==== b e g i n   i n s e r t i o n  =========================

# insert("Water glass",10,5)
# will keep adding this item no matter what - not so good.

# ==== s e t   u p   v i e w s  =========================

def view():
    conn=sqlite3.connect("lite.db")
    # create the cursor
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") # select all from store.
    rows=cur.fetchall() # store fetch in a variable called rows
    conn.close()
    return rows # will print as a list

# need a way to update/delete.

# ==== s e t   u p   d a t a   f u n c t i o n s  =========================

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    # that ending comma is very important!!
    # does a straight text search, removes ALL instances.
    conn.commit()
    conn.close()

def update(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=?" )

# delete("Water glass")  # removed every instance.
print(view())
