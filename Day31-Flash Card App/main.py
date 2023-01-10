from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/italian_words.csv")
data_dic = data.to_dict(orient="records")
current_card = {}

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dic)
    canvas.itemconfig(title_txt, text="Italian", fill="black")
    canvas.itemconfig(word_txt, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_txt, fill="white", text="Polish")
    canvas.itemconfig(word_txt, fill="white", text=current_card["Polish"])

def is_know():
    data_dic.remove(current_card)
    data.to_csv("words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BG_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
title_txt = canvas.create_text(400, 150, text="Title", font=("Ariel 40 italic"))
word_txt = canvas.create_text(400, 263, text="Word", font=("Ariel 60 bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(width=100, height=100, image=right_img,highlightthickness=0, command=is_know)
right_btn.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(width=100, height=100, image=wrong_img, highlightthickness=0, command=next_word)
wrong_btn.grid(column=1, row=1)

next_word()
window.mainloop()