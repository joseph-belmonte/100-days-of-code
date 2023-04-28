# working with GUIs
# and notes on key word arguments

import turtle
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    ''' changes text on label when button is clicked'''
    print("I got clicked")
    my_label.config(text="Button got clicked")
    new_text = input("Enter new text: ")


button = Button(text="Click me!", command=button_clicked)
button.pack()

# line always at end of program when working with GUIs
window.mainloop()

# *args allows you to pass in as many arguments as you want
# def add(*args):
#     ''' adds all numbers passed in as arguments'''
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# # **kwargs allows you to pass in as many keyword arguments as you want
# def calculate(**kwargs):
#     ''' allows you to pass in as many keyword arguments as you want'''
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
# calculate(add=3, multiply=5)
