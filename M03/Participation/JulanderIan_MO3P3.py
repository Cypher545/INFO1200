#!/usr/bin/env python3

# display a welcome message
print("Ian Julander's Rectangle App")
print()

# get input from the user and assign to variables
length = float(input("Please enter the length:\t"))
width = float(input("Please enter the width:\t\t"))

# create area variable and assign it the value of length times width
area = length * width

# create perimeter variable and assign it the value of 2 times length plus 2 times width
perimeter = (2 * length) + (2 * width)

print()
# display area
print("Area = " + str(area))
# display perimeter
print("Perimeter = " + str(perimeter))
print()
# exit message
print("Thank's for using this program!")