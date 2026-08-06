#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Anas AlSobeh
#Date: 08/05/2026
#Assignment #: M10 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.

# import module for csv
import csv

# declare filename constant
FILENAME = "contacts.csv"

# define display title function
def display_title():
    # program name
    print("Ian Julander's Contact Manager App")
    # blank line
    print()

# define menu function
def display_menu():
    # menu title
    print("COMMAND MENU")
    # blank
    print()
    # list command
    print("list - Display all contacts")
    # view command
    print("view - View a contact")
    # add command
    print("add - Add a contact")
    # delete command
    print("del - Delete a contact")
    # exit command
    print("exit - Exit program")

# define main function
def main():
    # create contacts variable and assign value from read contacts function
    contacts = read_contacts()
    # call title function
    display_title()
    # call menu function
    display_menu()
    # while loop for commands
    while True:
        # assign input to command variable
        command = input("Command: ")
        # if command is list call display function
        if command == "list":
            display(contacts)
        # if command is view call view function
        elif command == "view":
            view(contacts)
        # if command is add call add function
        elif command == "add":
            add(contacts)
        # if command is del call delete function
        elif command == "del":
            delete(contacts)
        # if command is exit exit program
        elif command == "exit":
            break
        # if invalid command display error message
        else:
            print("Not a valid command. Please try again.\n")
    # goodbye message
    print("Bye!")

# define display contacts function
def display(contacts):
    # checks to see if any contacts in list
    if len(contacts) == 0:
        # if not, display message
        print("There are no contacts in the list")
        # return
        return
    # if contacts in list
    else:
        # loop through contacts
        for i, row in enumerate(contacts, start=1):
            # display contact name and number
            print(f"{i}. {row[0]}")
        # blank
        print()

# define view function
def view(contacts):
    # assign contact number to number variable
    number = get_contact_number(contacts)
    # check if number greater than 0
    if number > 0:
        # uses index number to assign information to contact variable
        contact = contacts[number-1]
        # display contact name
        print("Name:", contact[0])
        # display contact email
        print("Email:", contact[1])
        # display contact phone number
        print("Phone:", contact[2])
        # blank line
        print() 

# define get contact number function
def get_contact_number(contacts):
    # while loop
    while True:
        # start exception handling
        try:
            # check if input is int
            number = int(input("Number: "))
        # if not, value error
        except ValueError:
            # error message
            print("Invalid integer.\n")
            # return invalid number
            return -1
        # check if input is out of range    
        if number < 1 or number > len(contacts):
            # if so error message
            print("Invalid contact number.\n")
            # return invalid number
            return -1
        # if valid
        else:
            # return the number
            return number

# define add contacts function
def add(contacts):
    # assign user input to name
    name = input("Name: ")
    # assign user input to email
    email = input("Email: ")
    # assign user input to phone
    phone = input("Phone: ")
    # initialize contact list
    contact = []
    # append name to list
    contact.append(name)
    # append email to list
    contact.append(email)
    # append phone number to list
    contact.append(phone)
    # append to file
    contacts.append(contact)
    # call writer function
    write_contacts(contacts)
    # confirmation message
    print(f"{contact[0]} was added.")
    # blank line
    print()

# define write contacts function
def write_contacts(contacts):
    # open csv file
    with open(FILENAME, "w", newline="") as file:
        # create writer object
        writer = csv.writer(file)
        # write
        writer.writerows(contacts)

# define delete contacts function
def delete(contacts):
    # get number from get contact number function
    number = get_contact_number(contacts)
    # if number is greater than 0
    if number > 0:
        # delete contact
        contact = contacts.pop(number-1)
        # confirmation message
        print(f"{contact[0]} was deleted.\n")
    # write to file
    write_contacts(contacts)

# define read contacts function
def read_contacts():
    # initialize contacts list
    contacts = []
    # while loop
    while True:
        # start exception handling
        try:
            # open csv file
            with open(FILENAME, newline="") as file:
                # create reader object
                reader = csv.reader(file)
                # loop through rows
                for row in reader:
                    # append contact info
                    contacts.append(row)
        # in case file isn't found
        except FileNotFoundError:
            # print missing file message
            print("Could not find contacts file! Starting new contacts file...")
        # return contacts
        return contacts

# if module is ran as main
if __name__ == "__main__":
    # call main
    main()