#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: Anas AlSobeh
#Date: 07/28/2026
#Assignment #: M07 Project P1
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.

# imports tkinter for gui
import tkinter as tk
# imports ttk and messagebox for gui
from tkinter import ttk
from tkinter import messagebox
# imports math for calculations
import math

# create main window
root = tk.Tk()
# set window size
root.geometry("250x225")
# window title
root.title('Hypotenuse Calculator')
# locks window size
root.resizable(False, False)

# create frame
frame = ttk.Frame(root, padding="10 10 12 12")
# pack frame to fill window
frame.pack(fill="both", expand=True)

# variable to store values of a, b, and c
a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()


# entry for side A
a_entry = ttk.Entry(frame, textvariable=a)
# align entry
a_entry.grid(column=0, row=1)

# label for side A
a_label = ttk.Label(frame, text='Enter side A:')
# align label
a_label.grid(column=0, row=0)

# label for side B
b_label = ttk.Label(frame, text='Enter side B:')
# align label
b_label.grid(column=0, row=2)

# entry for side B
b_entry = ttk.Entry(frame, textvariable=b)
# align entry
b_entry.grid(column=0, row=3)

# create function to determine C
def Pythagorean():
    # get value of a
    a_value = float(a_entry.get())
    # get value of b
    b_value = float(b_entry.get())
    # calculate C using Pythagorean theorem
    c_value = math.sqrt(a_value**2 + b_value**2)
    # sets to 3 decimal places
    c.set(f"{c_value:.3f}")

# create button to calculate
calculate_button = ttk.Button(frame, text="Calculate", command=Pythagorean)
# align button
calculate_button.grid(column=0, row=4, padx=30, pady=10)

# label for c
c_label = ttk.Label(frame, text='Hypotenuse:')
# align label
c_label.grid(column=0, row=5, padx=30, pady=5)

# read only to display C
c_display = ttk.Entry(frame, textvariable=c, state='readonly')
# align display
c_display.grid(column=0, row=6, padx=30, pady=5)
# loop for display
root.mainloop()