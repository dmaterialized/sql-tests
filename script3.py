# / database loader - creates a postgresql database using psycopg2.
# \
# / version: 0.1
# \ date: 2017.05.07
# / initial: 2017.05.07
# \ TODO:
# / -
# \ -
# / -
# \ -
# / -


import psycopg2

# going to do this entire thing in a Create function.

def create_table():
    # ====  i n i t    d a t a b a s e  =====================
    # - first create the database
    conn=psycopg2.connect("dbname='postgrestest' user='postgres' password='sql72270' host='/tmp/' port='5432'")
# establish connection

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

# ==== t e s t   i n s e r t i o n  =========================

# insert("Water glass",10,5)
# will keep adding this item no matter what - not so good.

# ==== s e t   u p   v i e w s  =========================

def view():
    conn=psycopg2.connect("dbname='postgrestest' user='postgres' password='sql72270' host='/tmp/'port='5432'")
    # create the cursor
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") # select all from store.
    rows=cur.fetchall() # store fetch in a variable called rows
    conn.close()
    return rows # will print as a list

def printResult():
    print("after update: ")
    print(view()) # check after update

# ==== s e t   u p   d a t a   f u n c t i o n s  =========================
# -------------------------------------------------------------------------
def insert(item,quantity,price): # ensure that you set the arguments here
    conn=psycopg2.connect("dbname='postgrestest' user='postgres' password='sql72270' host='/tmp/'port='5432'")

    # - create the cursor object
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

def delete(item):
    conn=psycopg2.connect("dbname='postgrestest' user='postgres' password='sql72270' host='/tmp/'port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    # that ending comma is very important!!
    # does a straight text search, removes ALL instances.
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='postgrestest' user='postgres' password='sql72270' host='/tmp/'port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=? price=? WHERE item=?",(quantity,price,item))
    # update quant + price of an item matching "item"
    # no comma at end is needed, because of multiple parameters
    conn.commit()
    conn.close()

# ==== e n d   d a t a   f u n c t i o n s  ================================
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
# ==== d e b u g   o p s ===================================================
# print("before update: ")
# print(view()) # check before update
# ==============================================

# push an update
update(11, 6.5, 'cup and saucer')
update(22, 35.50, 'state of affairs')
# maybe functionalize the below:
    # print("after update: ")
    # print(view()) # check after update
    # done!

printResult()

def curateCollection():
    # curate is going to move items into ordered lists
    conn=psycopg2.connect("store")
    cur=conn.cursor()

    # iterate through the items in row i
    conn.commit()
    conn.close()

create_table()
