'''Miles to Kilometer Converter'''

from tkinter import *

window = Tk()

window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=150)

# Entry
input_text = Entry(width=10)


# On Click Function
def button_clicked():
    ''' converts miles to kilometers'''
    miles = float(input_text.get())
    km = miles * 1.609
    converted_number.config(text=km)


# Button
convert_button = Button(text="Convert", command=button_clicked)

# Labels
base_units = Label(text="mi")
description = Label(text="is equal to")
converted_number = Label(text="0")
converted_units = Label(text="km")

# Grid
input_text.grid(column=1, row=0)
convert_button.grid(column=1, row=2)
base_units.grid(column=2, row=0)
description.grid(column=0, row=1)
converted_number.grid(column=1, row=1)
converted_units.grid(column=2, row=1)

# line always at end of program when working with GUIs
window.mainloop()
