from tkinter import *
import pandas as pd
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_list = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pd.read_csv("data/french_words.csv")
    word_list = og_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_list)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_back_img, image=front_bg)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    eng_word = current_card["English"]
    canvas.itemconfig(card_word, text=eng_word, fill="white")
    canvas.itemconfig(card_back_img, image=back_bg)

def known_words():
    word_list.remove(current_card)
    print(len(word_list))
    data_ = pd.DataFrame(word_list)
    data_.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Creating UI
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, func=flip_card)

# front canvas
canvas = Canvas(width=800, height=526)
front_bg = PhotoImage(file="images/card_front.png")
back_bg = PhotoImage(file="images/card_back.png")
card_back_img = canvas.create_image(400, 263, image=front_bg)

# Front text
card_title = canvas.create_text( 400, 150, text="",font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)
card_word = canvas.create_text( 400, 263, text="",font=("Arial", 60, "bold"))

# Front BG
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(text="Right", image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_button = Button(text="Right", image=wrong_image, highlightthickness=0, command=known_words)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
