from service import *
import db


print(
    """
    Welcome to the QA Cafe, what would you like to do? 
    1. Create an order
    2. Read an order
    3. Read all Orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    """
)

# print(service.getAll())

def choice():
    choice = int(input("Please choose between 1 and 6: "))
    print(choice)
    if choice == 1:
         create_record()
    elif choice == 2:
         read_an_order()
    elif choice == 3:
         read_all()
    elif choice == 4:
         print("Update an order")
    elif choice == 5:
         delete_an_order()
    elif choice == 6:
        delete_an_order()



def create_record():
    customer_name = input("Please enter your name: ")
    drink = input("What would you like to drink: ")
    size = input("How big do you want your drink: Small: Medium: Large: ")
    price = input("Please enter the cost: ")
    create_order(customer_name,drink,size,price)

def delete_orders():
    delete_all()

def read_an_order():
    id = input('please enter your order ID: ')
    read_Id(id)

def delete_an_order():
    id = input('Please enter an order id to delete that order: ')
    delete_order(id)

def read_all():
    get_all()





choice()