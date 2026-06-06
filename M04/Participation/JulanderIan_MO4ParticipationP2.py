#!/usr/bin/env python3

# display a welcome message
print("Welcome to Ian Julander's Future Value Calculator")
print()

# create variable for loop
choice = "y"
# start loop
while choice.lower() == "y":

    #create variable for loop
    is_valid = False
    while is_valid == False:

        # get input from user
        monthly_investment = float(input("Enter monthly investment:\t"))
        
        # validate monthly investment
        if monthly_investment > 0 and monthly_investment <= 1000:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 1000. Please try again.")
        
    # reset variable for loop    
    is_valid = False
    while is_valid == False:

        # get input from user
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        
        # validate yearly interest rate
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.")

    # reset variable for loop
    is_valid = False
    while is_valid == False:

        # get input from user
        years = int(input("Enter number of years:\t\t"))

        # validate years
        if years > 0 and years <= 50:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 30. Please try again.")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
