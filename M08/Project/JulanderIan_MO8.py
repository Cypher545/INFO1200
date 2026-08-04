#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Anas AlSobeh
#Date: 08/04/2026
#Assignment #: M08 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.

# display_title function
def display_title():
    # program name
    print("Ian Julander's Wizard Inventory Game")
    # blank line
    print()

# display_menu function
def display_menu():
    # display command menu
    print("COMMAND MENU")
    # blank
    print()
    # show
    print("show - Show all items")
    # grab
    print("grab - Grab an item")
    # edit
    print("edit - Edit an item")
    # drop
    print("drop - Drop an item")
    # exit
    print("exit - Exit program")
    # blank line
    print("")

# main function
def main():
    # call title function
    display_title()
    # call menu
    display_menu()
    # initial inventory list variable
    inventory = ["Extravagant Robe", "Scroll of Icarian Flight", "Colovian Fur Helm"]

# while loop until user exits
    while True:
        command = input("Command: ")
        # if user types show
        if command == "show":
            # display inventory
            show(inventory)
        # if user types grab
        elif command == "grab":
            # grab item
            grab_item(inventory)
        # if user types edit
        elif command == "edit":
            # edit item
            edit_item(inventory)
        # if user types drop
        elif command == "drop":
            # drop item
            drop_item(inventory)
        # if user types exit
        elif command == "exit":
            # exit loop
            break
        else:
            print("Not a valid command. Please try again.\n")
print("Bye!")

# function to show inventory
def show(inventory):
    # loop to loop through all items
    for number, item in enumerate(inventory, start=1):
        # display item number and name
        print(f"{number}. {item}")
        # blank line
        print("")

# grab function

def grab_item(inventory):
    # check if number of items is more than or equal to 4
    if len(inventory) >= 4:
        # display message
        print("You can't carry any more items. Drop something first.")
    else:
        # prompt for item name
        item = input("Name: ")
        # add to inventory
        inventory.append(item)
        # comfirmation message
        print(f"{item} was added.\n")

# edit function
def edit_item(inventory):
    # prompt for item number
    number = int(input("Number: "))
    # check if number is valid
    if number < 1 or number > len(inventory):
        # error message if not
        print("Invalid item number.\n")
    # if valid
    else:
        # prompt for name
        item = input("Updated name: ")
        # update inventory list
        inventory[number-1] = item
        # confirmation message
        print(f"Item number {number} was updated.\n")

# drop function
def drop_item(inventory):
    # prompt for number to drop
    number = int(input("Number: "))
    # check if valid
    if number < 1 or number > len(inventory):
        # error message if not
        print("Invalid item number.\n")
    # if valid
    else:
        # remove from inventory
        item = inventory.pop(number-1)
        # confirmation
        print(f"{item} was dropped.\n")


# if started as the main module
if __name__ == "__main__":
    # call main
    main()