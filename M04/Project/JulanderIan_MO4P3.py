#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Dr. Anas AlSobeh
#Date: 06/11/2026
#Assignment #: M05 Project P3
#By submitting this assignment, I declare that the source code contained in this assignment was written 
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, 
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment 
#instructions, nor obtained from a subscription service. I understand that copying any source code, 
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that 
#I will receive a zero on this project if I am found in violation of this policy.

# Welcome message
print("Ian Julander's Change App")
print()

# create infinite loop variable
choice = "y"
# start while loop
while choice.lower() == "y":
    # get user input for number of cents
    cents = int(input("Enter number of cents (0-99): "))
    print()

    # calculate max num of quarters
    quarters = round(cents // 25)
    # calculate remaining cents
    cents = cents % 25
    # calculate max num of dimes
    dimes = round(cents // 10)
    # calculate remaining cents
    cents = cents % 10
    # calculate max num of nickels
    nickels = round(cents // 5)
    # calculate remaining cents
    cents = cents % 5
    # calculate max num of pennies
    pennies = round(cents // 1)
    
    # display change to user
    print("Quarters: " + str(quarters))
    print("Dimes:    " + str(dimes))
    print("Nickels:  " + str(nickels))
    print("Pennies:  " + str(pennies))
    print()

    # get user input for loop
    choice = input("Continue? (y/n): ")
    print()

# end message
print("Bye!")