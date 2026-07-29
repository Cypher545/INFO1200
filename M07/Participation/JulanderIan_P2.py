# imports tkinter for gui
import tkinter as tk
# imports ttk and messagebox from tkinter for gui
from tkinter import ttk, messagebox

# create frame for the gui
root = tk.Tk()
# names program
root.title("Ian's Name Program")
# sets size of window
root.geometry("400x100")
frame = ttk.Frame(root)
frame.grid(column=0, row=0)

# label prompting user for name
promptLabel = tk.Label(root, text = "Enter your name:")
# sets label to top left of window
promptLabel.grid(row = 0, column = 0, sticky = tk.NW)

# create var for user name
userName = tk.StringVar()

# create text entry for user's name
userName = tk.Entry(root, width=30, textvariable=userName)
# sets text entry to top of window
userName.grid(row = 0, column = 1, sticky = tk.N)


# define button click
def buttonClick():
    # get user's name from text entry
    name = userName.get()
    # return user's name to label
    nameLabel.config(text=f"Your name is: {name}")

# create a button to display user's name
displayButton = tk.Button(root, text="Display Name", command=buttonClick).grid(column=1, row=1, sticky=tk.S)

# create a label to display user's name
nameLabel = tk.Label(root, text="")
# sets label to bottom of window
nameLabel.grid(column=1, row=2, sticky=tk.S)


# start main loop for gui
root.mainloop()