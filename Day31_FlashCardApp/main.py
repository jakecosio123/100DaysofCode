from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word_index = 0

# ----------------------- Flash Card setup -----------------------
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    word_bank = df.to_dict('records')
else:
    word_bank = df.to_dict('records')


def new_flash_card():
    global word_index
    max_index = len(word_bank) - 1
    word_index = random.randint(0, max_index)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(current_word, text=f"{word_bank[word_index]['French']}", fill="black")
    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(current_word, text=f"{word_bank[word_index]['English']}", fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(card_side, image=card_back_img)


def knows_word():
    del word_bank[word_index]
    words_to_learn = pandas.DataFrame(word_bank)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_flash_card()


# --------------------------- UI Setup ---------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

# set image variables
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_btn_img = PhotoImage(file="images/right.png")
wrong_btn_img = PhotoImage(file="images/wrong.png")

# create canvas with image as the background and text for flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
current_word = canvas.create_text(400, 263, text=f"", font=("Arial", 60, "bold"))
new_flash_card()
canvas.grid(column=0, row=0, columnspan=2)

# create buttons and display them on screen
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=new_flash_card)
wrong_btn.config(borderwidth=0)
wrong_btn.grid(column=0, row=1)
right_btn = Button(image=right_btn_img, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=knows_word)
right_btn.config(borderwidth=0)
right_btn.grid(column=1, row=1)

window.mainloop()
