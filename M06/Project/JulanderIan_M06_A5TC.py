#!/usr/bin/env python3

#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Dr. Anas AlSobeh
#Date: 07/08/2026
#Assignment #: M06 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written 
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, 
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment 
#instructions, nor obtained from a subscription service. I understand that copying any source code, 
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that 
#I will receive a zero on this project if I am found in violation of this policy.

# creates variable for tax rate and sets it to 6%
tax = 0.06

# defines function to calculate sales tax based on total cost
def sales_tax(total):
    # calculates sales tax by multiplying total cost by tax rate
    sales_tax = total * tax
    # returns calculated sales tax
    return sales_tax

# defines main function
def main():
    # display title of program
    print("Sales Tax Calculator\n")
    # prompts user for total cost as float and stores it in total variable
    total = float(input("Enter total: "))
    # creates variable for total after tax and calculates
    total_after_tax = round(total + sales_tax(total), 2)
    # displays total after tax
    print("Total after tax: ", total_after_tax)

# calls main function to run the program    
if __name__ == "__main__":
    main()
