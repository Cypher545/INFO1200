#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Anas AlSobeh
#Date: 07/30/2026
#Assignment #: M07 Project P2
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.

# import tkinter for gui
import tkinter as tk
from tkinter import ttk
import random

# Dice rolling program. Must have 7 controls

# set up for gui
root = tk.Tk()
root.title("Ian's Dice Roller")
# set size
root.geometry("500x250")
# frame for program
frame = ttk.Frame(root, padding="10 10 10 10")
# allow frame to expand
frame.pack(fill="both", expand=True)


#button click to roll

def rollClick():
    # get number of dice from entry
    numDice = diceAmount.get()
    # check if number of dice is valid
    try:
        numDice = int(numDice)
        # checks if num is less than or = 0
        if numDice <= 0:
            # raise error
            raise ValueError
    # in case of error, display message
    except ValueError:
        resultLabel.config(text = 'Please enter a valid whole number greater than 0.')
        # return
        return
    numDice = int(numDice)
    # roll dice and display results
    results = []
    # roll dice x times
    for i in range(numDice):
        # rolls a die
        roll = random.randint(1, 6)
        # append result to list
        results.append(roll)
    # display results
    resultLabel.config(text = f'Results: {results}')
    # display total
    totalLabel.config(text = f'Total: {sum(results)}')

# button click to exit
def exitClick():
    # destroy window
    root.destroy()

# label to prompt user for number of dice
diceAmountLabel = tk.Label(frame, text = 'How many dice do you want to roll?')
# place label in frame
diceAmountLabel.pack()

# entry for number of dice. make variable
diceAmountVar = tk.StringVar()
# set up entry
diceAmount = tk.Entry(frame, textvariable=diceAmountVar)
# place in frame
diceAmount.pack()

# readonly label showing dice results
resultLabel = tk.Label(frame, text = 'Results: ')
# place in frame
resultLabel.pack()

# readonly label showing total
totalLabel = tk.Label(frame, text = 'Total: ')
# place in frame
totalLabel.pack()

# button for rolling dice
# chooses command and text for roll
rollButton = tk.Button(frame, text = 'Roll Dice', command = rollClick)
# place in frame
rollButton.pack()

# exit button 
# chooses command and text for exit
exitButton = tk.Button(frame, text = 'Exit', command = exitClick)
# place in frame
exitButton.pack()

# I can't think of another control to add. Since labels count, I'm just putting a
# nice message here. :)

messageLabel = tk.Label(frame, text = 'Thanks for using my program. :)')
# place in frame
messageLabel.pack()

# mainloop
root.mainloop()