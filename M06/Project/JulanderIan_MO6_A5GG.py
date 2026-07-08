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

# imports random module
import random

# defines function to display title of the program
def display_title():
    # displays title of the program
    print("Guess the number!")
    # blank line
    print()

# defines function to get the max range of number
def get_limit():
    # prompts user for upper limit and stores in limit variable
    limit = int(input("Enter the upper limit for the range of numbers: "))
    # returns limit
    return limit

# defines game function
def play_game(limit):
    # generates random number between 1 and limit
    number = random.randint(1, limit)
    # displays message to user about the range of numbers
    print(f"I'm thinking of a number from 1 to {limit}\n")
    # creates and sets count variable to track guesses
    count = 1

    # start while loop for guessing game
    while True:
        # prompts user for their guess and stores it in guess variable
        guess = int(input("Your guess: "))
        # checks if guess is too low and adds to count if so
        if guess < number:
            print("Too low.")
            count += 1
        # checks if guess is too high and adds to count if so
        elif guess > number:
            print("Too high.")
            count += 1
        # if guess is correct, displays number of tries
        elif guess == number:
            print(f"You guessed it in {count} tries.\n")
            # exits function
            return

# defines main function
def main():
    # calls function to display title of program
    display_title()
    
    # creates again variable and sets to y
    again = "y"
    # starts while loop to allow user to play (again)
    while again.lower() == "y":
        # calls function to get upper limit and stores in limit variable
        limit = get_limit()
        # calls function to play and passes limit variable
        play_game(limit)
        
        # prompts user to play again
        again = input("Play again? (y/n): ")
        # blank line
        print()
    # displays goodbye message
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

