from db import *


def get_all():
    data = view_all_records()
    return data

def create_order (customer_name, drink, size, price):
    insert_str = f"INSERT INTO cafe (customer_name, drink, size, extras, price) VALUES ('{customer_name}','{drink}','{size}','{price}');"
    runQuery(insert_str)
    show_str = f"SELECT cafe FROM ,my_cafe_db (customer_name, drink, size, extras, price) VALUES ('{customer_name}','{drink}','{size}','{price}');"
    runQuery(show_str)
    return True

def read_by_id(id):
    query = f'SELECT * FROM orders WHERE order_id = {id};'
    data = runQuery(query)
    return data

def delete_order(id):
    query = f'DELETE FROM orders WHERE order_id = {id};'
    delete_order(query)
    



