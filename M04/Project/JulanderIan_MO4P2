#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Dr. Anas AlSobeh
#Date: 06/10/2026
#Assignment #: M05 Project P2
#By submitting this assignment, I declare that the source code contained in this assignment was written 
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, 
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment 
#instructions, nor obtained from a subscription service. I understand that copying any source code, 
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that 
#I will receive a zero on this project if I am found in violation of this policy.

# Welcome message
print("Ian Julander's Tip Calculator")

# create and set variables for pre-defined tip percentages
tip_percentage_15 = 15
tip_percentage_20 = 20
tip_percentage_25 = 25

print()

# get user input for meal cost
meal_cost = float(input("Cost of meal: "))
print()

# display meal cost
print("Cost of meal:\t" + str(meal_cost))
print()

# calculate and display tip amounts
for i in [tip_percentage_15, tip_percentage_20, tip_percentage_25]:
    print(str(i) + "%")
    # calculate tip percentage
    tip_percent = i / 100
    # calculate tip amount
    tip_amount = meal_cost * tip_percent
    # round tip amount to 2 decimal places
    tip_amount = round(tip_amount, 2)
    # calculate total cost including tip
    total = meal_cost + tip_amount
    # round total to 2 decimal places
    total = round(total, 2)
    # display tip amount and total cost
    print("Tip amount:\t" + str(tip_amount))
    print("Total cost:\t" + str(total))
    print()
