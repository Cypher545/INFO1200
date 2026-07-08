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

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}\n")

    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess >= number:
            print("Too high.")
            count += 1
        elif guess == number:
            print(f"You guessed it in {count} tries.\n")
            return

def main():
    display_title()
    
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game()
        
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

