"""
Excercise 11.7

Question 3: Design a menu-based program that uses a dictionary to track the stock of
products in a store. The program should allow the user to:

(a) Add a new product.
(b) Update the stock of an existing product.
(c) Check the stock of a given product.
(d) Display all products and their current stock levels.
(e) Exit the program.

Error cases to be handled:
    • The user tries to add a product that already exists.
    • The user attempts to update or check stock for a product that does not exist.
"""

stock = {}

def add_product():
    prod = input("Enter name of product: ")
    if prod in stock:
        print("Product already exists in stock")
    else:
        stock[prod] = 0
        print(f"{prod} added to stock successfully")

def update_product():

    while (prod := input("Enter name of product: ")) not in stock:
        print(f"{prod} not in stock")
    amt = int(input(f"Current stock is {stock[prod]}. Enter new stock: "))
    stock[prod] = amt
    print(f"updated stock of {prod}")

def check_stock():
    while (prod := input("Enter name of product: ")) not in stock:
        print(f"{prod} not in stock")
    print(f"stock of {prod}: {stock[prod]}.")

def display_stock():

    if not stock:
        print("Stock is currently empty.")
        return

    for prod, amt in stock.items():
        print(f"{prod}: {amt}")

menu = "MENU\n1. Add product(default stock = 0)\n2. Update product stock\n3. Check stock of a product\n4. Display entire stock\n5. Exit\nOption (Input 1/2/3/4/5): "
while True:
    opt = int(input(menu))

    match opt:
        case 1:
            add_product()
        case 2:
            update_product()
        case 3:
            check_stock()
        case 4:
            display_stock()
        case 5:
            break
        case _:
            print("Invalid menu option. Try again")
    input("Press Enter to continue")

