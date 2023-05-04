''' This is the main file for the flash card app.'''

import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Portuguese"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/portuguese_words.csv")
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = data.to_dict(orient="records")


def next_card():
    '''Changes the word on the flash card to a random word from the csv file.'''
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(language_dict)
    canvas.itemconfig(card_title, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE], fill="black")
    canvas.itemconfig(card_img, image=front_card_img)
    window.after(3000, func=flip_card)


def flip_card():
    '''Flips the flash card to show the translation.'''
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=back_card_img)


def is_known():
    '''Removes the current card from the csv file.'''
    language_dict.remove(current_card)
    data = pd.DataFrame(language_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Jailbreak Anki")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# images
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")


# canvas allows us to layer things on top of each other
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text="", font=(
    "Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=(
    "Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# CREATE A BUTTON WITH TKINTER
wrong_button = Button(
    image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2)
right_button = Button(
    image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=2)

next_card()

window.mainloop()
