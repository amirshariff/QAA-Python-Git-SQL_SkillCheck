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
         print("Read an order")
    elif choice == 3:
         print("Read all Orders")
    elif choice == 4:
         print("Update an order")
    elif choice == 5:
         print("Delete an order")
    elif choice == 6:
        print("Delete all orders")



def create_record():
    customer_name = input("Please enter your name: ")
    drink = input("What would you like to drink: ")
    size = input("How big do you want your drink: Small: Medium: Large: ")
    price = input("Please enter the cost: ")
    create(customer_name,drink,size,price)

choice()