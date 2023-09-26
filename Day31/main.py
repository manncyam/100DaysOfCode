from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000
WORD_TO_LEARN_FILE = "./data/words_to_learn.csv"
MADARIN_WORD_TO_LEARN = "./data/mandarin_words_to_learn.csv"

current_word = None
timer_handler = None

try:
    df = pd.read_csv(MADARIN_WORD_TO_LEARN)
except FileNotFoundError:
    df = pd.read_csv("./data/mandarin_words.csv")
finally:
    words = {} if len(df) == 0 else df.to_dict(orient="records")
    
def flip_card(word):
    language = [k for k in word][1]
    canvas.itemconfig(card_title, text=language, fill="white")
    canvas.itemconfig(card_word, text=word[language], fill="white")
    canvas.itemconfig(card, image=back_image)

def next_card():
    global current_word, timer_handler
    
    window.after_cancel(timer_handler)
    if len(words) == 0:
        return
    current_word = random.choice(words)

    language = [k for k in current_word][0]
    canvas.itemconfig(card_title, text=language, fill="black")
    canvas.itemconfig(card_word, text=current_word[language], fill="black")
    canvas.itemconfig(card, image=front_image)
    
    timer_handler = window.after(TIMER, flip_card, current_word)
    
def save_to_learn_word():    
    df = pd.DataFrame(words)
    df.to_csv(MADARIN_WORD_TO_LEARN, index=False)

def is_known():
    words.remove(current_word)
    save_to_learn_word()
    next_card()

def is_unknown():
    next_card()

window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Curier", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Curier", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="./images/wrong.png")
checked_image = PhotoImage(file="./images/right.png")

x_btn = Button(image=x_image, command=is_unknown, highlightthickness=0)
x_btn.grid(row=1, column=0)

checked_btn = Button(image=checked_image, command=is_known ,highlightthickness=0)
checked_btn.grid(row=1, column=1)

timer_handler = window.after(0, next_card)

window.mainloop()