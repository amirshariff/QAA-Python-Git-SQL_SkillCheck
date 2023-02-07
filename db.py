import sqlite3 as sql
from service import *

# Connection - Where is the database stored, and any passwords needed
# Cursor - Virtual tool to navigate a DB 
# Query - What request / query are we sending to the DB 

# Connect to test-db, if it doesn't exist it creates it  
conn = sql.connect("my_cafe_db")

# Create our cursor, which is a function which is part of connection
cursor = conn.cursor()

# Python is reading our sql file and saving a String of content
sql_file = open("orders.sql")
sql_string = sql_file.read()
# Python is running this SQL string inside of our DB 
#cursor.executescript(sql_string)

def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def view_all_records():
    query = 'SELECT * FROM my_cafe;'
    data = runQuery(query)
    return data

def createOrder(customer_name, drink, size, price):
    query = f"INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('{customer_name}', '{drink}', '{size}', '{price}');"
    runQuery(query)
 

def viewAnOrder(id):
    query= f"SELECT * FROM orders WHERE order_id = {id}"
    runQuery(query)


       

# Saving the data into the db created via cursor stuff
conn.commit()