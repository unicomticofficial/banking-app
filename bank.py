import os

def get_customer_info():
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    username = input('Enter the username: ')
    password = input('Enter the password: ')

    return [name, address, username, password]

def create_customer_next_id():
    with open("customers.txt", "r") as customer_file:
        # print(int(customer_file.readlines()[-1].split(",")[0][1:]) + 1)
        return f"U{int(customer_file.readlines()[-1].split(",")[0][1:]) + 1:03}"

create_customer_next_id()
        

# def create_customer():
#     customers = get_customer_info()
#     with open("customers.txt", "a") as file:
#         file.write(f"{customers[0]},{customers[1]}\n")

# def create_user():
#     customers = get_customer_info()
#     with open("users.txt", "a") as file:
#         file.write(f"{customers[2]},{customers[3]}\n")

def create_customer_and_user():
    customers = get_customer_info()
    
    with open("customers.txt", "a") as customer_file, open("users.txt", "a") as user_file:
        customer_file.write(f"{create_customer_next_id()},{customers[0]},{customers[1]}\n")
        user_file.write(f"{customers[2]},{customers[3]}\n")

def view_all_customers():
    with open("customers.txt", "r") as customer_file:
        for customer in customer_file.readlines():
            print(customer)

print('Press\n 1. for Create Customer \n 2. for View all customers')

get_input = int(input('Enter the number: '))

if get_input == 1:
    create_customer_and_user()
elif get_input == 2:
    view_all_customers()

    
