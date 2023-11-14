import sqlite3
global c
conn = sqlite3.connect('tests.db')
c = conn.cursor()
# connect to database + create a cursor
def connect_DB():

    conn = sqlite3.connect('tests.db')
    #c = conn.cursor()
    
def input_into_DB(first_name, last_name , age):
    connect_DB()
    c.execute("INSERT INTO customer VALUES(?,?,?)",(first_name,last_name,age))
    print("command executed successfully")
    Commit_N_Close()

#query the database
def output_DB():
    connect_DB()
    c.execute("SELECT rowid, * FROM customer")
    #output from database and format
    items = c.fetchall()
    for item in items:
        print(item[1] + "\t" + item[2] + "\t" + str(item[3]) +"\t" + str(item[0]))
    Commit_N_Close()

# updating values
def update_FirstNameDB(new_value, rowid_):
    connect_DB()
    c.execute("UPDATE customer SET first_name = new_value WHERE rowid = ?", (rowid_))
    Commit_N_Close()
def update_LastNameDB(new_value, rowid_):
    connect_DB()
    c.execute ("UPDATE SET last_name = new_value WHERE rowid = ?",(rowid_))
    Commit_N_Close
def update_AgeDB(newvalue,rowid_):
    connect()
    c.execute("UPDATE SET last_name = new_value WHERE rowid = ?",(rowid_))
    Commit_N_Close()

#deleting records
def delete_DB_rowid(rowid_): 
    connect_DB()
    c.execute("DELETE from customer WHERE rowid = ?",(rowid_))
    COmmit_N_Close()


#order by decending
def order_by_item_DB(item):
    connect_DB()
    c.execute("SELECT rowid, * FROM customer ORDER BY ?",(item))
    items = c.fetchall()
    for item in items:
        print(item)
    Commit_N_Close()

#create a table (3)
#c.execute("""CREATE TABLE customer (first_name text, last_name text, age int)""")
def Commit_N_Close():
    #commit our connection
    conn.commit()
    #close our connection
    conn.close()



input_into_DB("Zack","Long", 23)
output_DB()
