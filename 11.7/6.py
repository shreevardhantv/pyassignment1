"""
Excercise 11.7

Question 6: Create a telephone directory using a dictionary. The name of the individ-
ual and the telephone number will be key and value, respectively. Write a
Python program that allows the user to perform the following operations:
(a) Add a Contact: Add a new contact with a name and phone number
to the directory.
(b) Update a Contact: Update the phone number of an existing contact.
(c) Delete a Contact: Remove a contact from the directory.
(d) Search for a Contact: Look up the phone number of a contact by
their name.
(e) Display All Contacts: Print all contacts in the directory.
(f) Exit the program.

Use a menu-driven approach.
"""

directory = {}

def add_contact():
    if (name := input("Enter contact name: ")) in directory:
        print(f"{name} already exists in the directory.")
    else:
        phone = input("Enter phone number: ")
        directory[name] = phone
        print(f"Contact {name} added successfully.")

def update_contact():
    while (name := input("Enter contact name to update: ")) not in directory:
        print(f"{name} does not exist in the directory.")
    phone = input(f"Current number for {name} is {directory[name]}. Enter new number: ")
    directory[name] = phone
    print(f"Contact {name} updated successfully.")

def delete_contact():
    while (name := input("Enter contact name to delete: ")) not in directory:
        print(f"{name} does not exist in the directory.")
    del directory[name]
    print(f"Contact {name} deleted successfully.")

def search_contact():
    while (name := input("Enter contact name to search: ")) not in directory:
        print(f"{name} does not exist in the directory.")
    print(f"Phone number for {name}: {directory[name]}.")

def display_contacts():
    if not directory:
        print("The directory is empty.")
        return
    print("Contacts in the directory:")
    for name, phone in directory.items():
        print(f"{name}: {phone}")

menu = "MENU\n1. Add Contact\n2. Update Contact\no. Delete Contact\n4. Search for Contact\n5. Display All Contacts\n6. Exit\nOption (Input 1/2/3/4/5/6): "

while True:
    option = int(input(menu))
    match option:
        case 1:
            add_contact()
        case 2:
            update_contact()
        case 3:
            delete_contact()
        case 4:
            search_contact()
        case 5:
            display_contacts()
        case 6:
            break
        case _:
            print("Invalid menu option. Try again")
    input("Press Enter to continue")
3