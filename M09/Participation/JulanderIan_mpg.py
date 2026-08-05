#!/usr/bin/env python3

# import csv to use csv files
import csv

# define constant for file name
FILENAME = "trips.csv"

# define write trips function
def write_trips(trips):
    # write trips to csv
    with open(FILENAME, "w", newline="") as output_file:
        # create csv writer object
        writer = csv.writer(output_file)
        # write trips to file
        writer.writerows(trips)

# define read trips function
def read_trips():
    # initialize trips list
    trips = []
    # read trips from csv
    with open(FILENAME, "r", newline="") as input_file:
        # create csv reader object
        reader = csv.reader(input_file)
        # loop through rows
        for row in reader:
            # append row to list
            trips.append(row)
        # turn trips list
        return trips

# define list trips function
def list_trips(trips):
    # print headers and format
    print("Distance\tGallons\t\tMPG")
    # loop through trips
    for i in range(0, len(trips)):
        # get trip from list an assign to trip variable
        trip = trips[i]
        # print trip information
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
    # blank line
    print()

# define get miles function
def get_miles_driven():
    # prompt for user input and validate miles driven
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:
        # display error if not valid                    
        print("Entry must be greater than zero. Please try again.\n")
    # return miles driven       
    return miles_driven

# define get gallons function          
def get_gallons_used():
    # prompt for gallons used and validate
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:
        # print error if not valid                    
        print("Entry must be greater than zero. Please try again.\n")
    # return gallons used
    return gallons_used

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    # blank
    print()

    # 2D list for trips
    trips = read_trips()
    # list trops
    list_trips(trips)
    # assign more to y for loop
    more = "y"
    # loop to get miles driven and gallons used
    while more.lower() == "y":
        # get miles driven
        miles_driven = get_miles_driven()
        # get gallons used
        gallons_used = get_gallons_used()
        # calculate mpg and round to 2 places                         
        mpg = round((miles_driven / gallons_used), 2)
        # print mpg
        print(f"Miles Per Gallon:\t{mpg}")
        # blank line
        print()

        # create single trip variable to hold information
        single_trip = [miles_driven, gallons_used, mpg]
        # append single trip to trips list
        trips.append(single_trip)
        # write trips to csv file
        write_trips(trips)
        # prompt user to continue or not
        more = input("More entries? (y or n): ")
    # exit message
    print("Bye!")
# if main module
if __name__ == "__main__":
    # call main
    main()

