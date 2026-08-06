#!/usr/bin/env python3

# define get number function        
def get_number(prompt, low, high):
    # start loop
    while True:
        # exception handling
        try:
            # makes sure number is a float
            number = float(input(prompt))
        # raise exception if number is not valid
        except:
            # print error message
            print("Invalid entry. Please enter a number.")
            # continues instead of crashing
            continue
        #if number > low and number <= high:
            #is_valid = True
            #return number
        # if number is outside of range
        else:
            # error if too low
            print(f"Entry must be greater than {low} "
                  # error if too high 
                  f"and less than or equal to {high}.")
# define get integer function            
def get_integer(prompt, low, high):
    # start loop
    while True:
        # exception handling
        try:
            # makes sure number is an integer
            number = int(input(prompt))
        # if not, raises exception
        except:
            # print error message
            print("Invalid entry. Please enter a number.")
            # continues instead of crashing
            continue
        #if number > low and number <= high:
            #is_valid = True
            #return number
        # checks if number is in range
        else:
            # error message if too low
            print(f"Entry must be greater than {low} "
                  # error if too high 
                  f"and less than or equal to {high}.")

# define calculation function
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    # convert to months
    months = years * 12

    # calculate future value
    future_value = 0.0
    # loops through the amount of months calculated
    for i in range(months):
        # adds monthly investment to future value
        future_value += monthly_investment
        # calculates monthly interest
        monthly_interest = future_value * monthly_interest_rate
        # adds interest calculated to value
        future_value += monthly_interest
    # returns the value
    return future_value

# define main function
def main():
    # choice set to y for loop
    choice = "y"
    # start while loop
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        # for interest rate
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        # for years
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        # blank line
        print()
        # display future value. Rounds to two decimal places.
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        # blank line
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        # blank line
        print()
    # goodbye message
    print("Bye!")
    
if __name__ == "__main__":
    main()
