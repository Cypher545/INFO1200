#!/usr/bin/env python3

# welcome message module
def display_welcome():
    # name of program
    print("The Test Scores program")
    # tells user how to exit
    print("Enter 'x' to exit")
    # ""
    print("")

def get_scores():
    # creates new variable for list
    scores = []
    # loop to get scores from user
    while True:
        # prompt for score and assign to variable
        score = input("Enter test score: ")
        # check if user wants to exist
        if score == "x":
            # return scores
            return  scores
        # check if valid
        else:
            # convert to int
            score = int(score)
            # check if score is within range of 0-100
            if score >= 0 and score <= 100:
                # if yes, add to list
                scores.append(score)
            # if not valid
            else:
                # error message
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # sort the list of scores
    scores.sort()
    # calculate total scores
    total = 0
    # loop through list of scores
    for score in scores:
        # add each to total
        total += score
    # variable for number of scores
    num_scores = len(scores)
    # variable for min
    min_score = min(scores)
    # variable for max
    max_score = max(scores)
    # variable for median
    median = 0
    # variable for median index
    median_index = len(scores) // 2
    # check if number of scores is odd
    if num_scores % 2 == 1:
        # if odd, median is middle value
        median = scores[median_index]
    else:
        # if even take first middle value
        middle_1 = scores[median_index]
        # and second middle value
        middle_2 = scores[median_index - 1]
        # calculate median
        median = (middle_1 + middle_2) / 2


    # calculate average score
    average = total / num_scores
    
    # format and display the result
    print()
    # format and display
    print("Score total:       ", total)
    # format and display
    print("Number of Scores:  ", num_scores)
    # format and display
    print("Average Score:     ", average)
    # format and display
    print("Min:               ", min_score)
    # format and display
    print("Max:               ", max_score)
    # format and display
    print("Median:            ", median)

# main function
def main():
    # call welcome message
    display_welcome()
    # call get_scores and assign to variable
    scores = get_scores()
    # call process_scores and pass scores
    process_scores(scores)
    # blank line
    print("")
    # goodbye message
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

