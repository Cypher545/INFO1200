#!/usr/bin/env python3

# import csv to use csv files
import csv

# define constant for file name
FILE_NAME = "trips.csv"

# define miles driven function
def get_miles_driven():
    # prompt for miles driven and validate
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:
        # if invalid print error            
        print("Entry must be greater than zero. Please try again.\n")
    # return miles driven       
    return miles_driven

# define gallons used function          
def get_gallons_used():
    # prompt for gallons used and validate
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:
        # if invalid print error                    
        print("Entry must be greater than zero. Please try again.\n")
    # return gallons used    
    return gallons_used

# define main function        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    # blank
    print()

    # initialize trips list
    trips = []

    # set more to y for loop
    more = "y"
    # loop to get miles driven and gallons used
    while more.lower() == "y":
        # get miles driven
        miles_driven = get_miles_driven()
        # get gallons used
        gallons_used = get_gallons_used()

        # calculate mpg and assign to mpg variable. Round to 2 places                         
        mpg = round((miles_driven / gallons_used), 2)
        # display mpg
        print(f"Miles Per Gallon:\t{mpg}")
        # blank
        print()

        # create single trip to hold trip information
        single_trip = [miles_driven, gallons_used, mpg]
        # append to trips list
        trips.append(single_trip)
        # input to see if user wants to continue
        more = input("More entries? (y or n): ")
    # write trips to csv file
    with open(FILE_NAME, "w", newline="") as output_file:
        # create writer object
        writer = csv.writer(output_file)
        # write header row for readability
        writer.writerow(["Miles Driven", "Gallons Used", "Miles Per Gallon"])
        # write trips to file
        writer.writerows(trips)

    # display goodbye message
    print("Bye!")

# if main module
if __name__ == "__main__":
    # call main
    main()

