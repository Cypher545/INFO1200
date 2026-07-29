#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Anas AlSobeh
#Date: 07/28/2026
#Assignment #: M09 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.

import csv

#define read_sales() function
def read_sales():
    # create a new variable named sales and assign it the value of read_sales() function
    sales = []
    # open file
    with open('monthly_sales.csv', newline='') as file:
        # create reader
        reader = csv.reader(file)
        # read rows
        for row in reader:
            sales.append(row)
    return sales

# define display_title() function
def display_title():
    # display title and name
    print("Ian Julander's Monthly Sales")
    # blank line
    print()

# define a display_menu() function
def display_menu():
    # display command menu
    print("COMMAND MENU")
    # display commands
    print("monthly\t- View monthly sales")
    print("yearly\t- View yearly summary")
    print("edit\t- Edit sales for a month")
    print("exit\t- Exit program")
    print()
    

# create a view_monthly_sales() function that receives the sales as a parameter
def view_monthly_sales(sales):
    # create a foew loop that loops through all items
    for row in sales:
        print(f"{row[0]} - {row[1]}")
    # blank line
    print()

# create a view_yearly_summary() function that recieves the sales as a parameter
def view_yearly_summary(sales):
    # create a total variable and set to 0
    total = 0
    # create a for loop that loops through each row in the sales
    for row in sales:
        amount = int(row[1])
        #add to the total
        total += amount

    # get count
    count = len(sales)
    
    # calculate average
    average = total / count
    # round to 2 decimal places
    average = round(average, 2)

    # format and display the result
    print("Yearly total:    ", total)
    print("Monthly average: ", average)        
    print()

# create an edit(sales) function that receives the sales as a parameter
def edit(sales):
    # create a new variable named "names" and assign it to as list of abrv months
    names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # create name variable and assign it the user's input for month
    name = input("Enter a month (Jan - Dec: ")
    name = name.title()
    # if the input does not exist in the names list, display error
    if name not in names:
        print("Invalid three-letter month.")
        print()
    else:
        # create a variable named "index" and assign it the value of index of month entered
        index = names.index(name)
        # create a variable in the if statement named "amount" and assign it the value of an int from user's input
        amount = int(input("Sales Amount: "))
        # create a month variable and assign empty list
        month = []
        # append the name to the list as well as amount
        month.append(name)
        month.append(str(amount))
        # add the month and amount to sales list at index
        sales[index] = month
        # call write_sales method
        write_sales(sales)
        # Show the text "Sales amount for {month[0]} was modified."
        print(f"Sales amount for {month[0]} was modified.")
        # blank line
        print()

# create write_sales function
def write_sales(sales):
    # open file
    with open('monthly_sales.csv', "w", newline='') as file:
        # open writer
        writer = csv.writer(file)
        writer.writerows(sales)

# define a main() function
def main():
    # call display_title() function
    display_title()
    # call display_menu() function
    display_menu()
    # call read_sales
    sales = read_sales()
    # create a while loop that executes until the user types exit
    while True:
        # create command variable and assign user input
        command = input("Command: ")
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "yearly":
            view_yearly_summary(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

# call main()
if __name__ == "__main__":
    main()