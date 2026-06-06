#!/usr/bin/env python3

# display a welcome message
print("Ian Julander's Miles per Gallon application")
print()

# create variable for loop
another_trip = "y"

# start loop
while another_trip.lower() == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    print()

    # start loop for input validation
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        # calculate total gas cost
        total_gas_cost = round((gallons_used * cost_per_gallon), 1)
        # calculate cost per mile
        cost_per_mile = round((total_gas_cost / miles_driven), 1)
        
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_mile)
        print()
    
    # ask user if they want to calculate another trip
    another_trip = input("Get entries for another trip (y/n)? ")
    print()

print()
print("Bye")



