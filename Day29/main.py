''' Local Password Manager '''
from tkinter import *
from tkinter import messagebox
import string
import pyperclip
from random import *

# CONSTANTS
PASSWORD_LENGTH = 16
SYMBOLS = "!@#$%^&*()_+"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # clear the password input
    password_input.delete(0, END)
    chars = choices(string.ascii_letters, k=randint(8, 10))
    chars += choices(string.digits, k=randint(2, 4))
    chars += choices(SYMBOLS, k=randint(2, 4))
    shuffle(chars)     # shuffle modifies argument and RETURNS NONE!!!
    rnd_string = "".join(chars)
    # insert the generated password into the password input
    password_input.insert(0, rnd_string)
    pyperclip.copy(rnd_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    ''' Save the password to a data.txt file'''
    website = website_input.get()
    email = UN_input.get()
    password = password_input.get()

    # validate inputs
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
        return

    else:
        # get user confirmation
        is_ok = messagebox.askokcancel(
            title="", message=f"{website}", detail=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            # open a file in append mode
            with open("data.txt", "a", encoding="utf-8") as f:
                # write the data to the file
                f.write(f"{website} | {email} | {password}\n")
                # close the file
                f.close()
                # clear the inputs
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.geometry("600x500")

lock_img = PhotoImage(file="logo.gif")
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)

canvas.grid(column=1, row=0)


# CREATE A LABEL WITH TKINTER
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
# focus the cursor on the website input
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
UN_label = Label(text="Email/Username:")
UN_label.grid(column=0, row=2)
UN_input = Entry(width=35)
UN_input.insert(0, "example@gmail.com")
UN_input.grid(column=1, row=2, columnspan=2, sticky="EW")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="EW")
password_input = Entry(width=20)
password_input.grid(column=1, row=3, sticky="EW")

# CREATE A BUTTON WITH TKINTER
generate_password_button = Button(
    text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
