from db import *

def create (customer_name, drink, size, extras, price):
    insert_str = f"INSERT INTO cafe (customer_name, drink, size, extras, price) VALUES ('{customer_name}','{drink}','{size}','{extras}','{price}');"
    runQuery(insert_str)
    show_str = f"SELECT cafe FROM ,my_cafe_db (customer_name, drink, size, extras, price) VALUES ('{customer_name}','{drink}','{size}','{extras}','{price}');"
    runQuery(show_str)
    return True

def read_by_id(id):
    order_data = runQuery(id)
    order = order(order_data) 
    return order_data


    



