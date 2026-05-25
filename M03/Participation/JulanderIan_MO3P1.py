#!/usr/bin/env python3

# display a welcome message
print("Ian Julander's MPG Calculator")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate and round miles per gallon
mpg = round(miles_driven / gallons_used, 1)

# calculate and round total cost
total_cost = round(gallons_used * cost_per_gallon, 1)

# calculate and round cost per mile
cost_per_mile = round(total_cost / miles_driven, 1)

# format and display the results
print()
# displays miles per gallon
print("Miles Per Gallon:\t\t" + str(mpg))
# displays total cost
print("Total Gas Cost:\t\t\t" + str(total_cost))
# displays cost per mile
print("Cost Per Mile:\t\t\t" + str(cost_per_mile))
print()
# display a goodbye message
print("Bye")


