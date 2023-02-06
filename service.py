from db import runQuery

def read_by_id(id):
    order_data = runQuery(id)
    order = order(order_data) 
    return order_data

def create (customer_name, drink, size, extras, price):
    insert_str = f"INSERT INTO cafe (customer_name, drink, size, extras, price) VALUES ('{customer_name}','{drink}','{size}','{extras}','{price}');"
    runQuery(insert_str)
    show_str = f"SELECT cafe FROM cafe-db (customer_name, drink, size, extras, price) VALUES ('{customer_name}','{drink}','{size}','{extras}','{price}');"
    runQuery(show_str)
    return True
    



