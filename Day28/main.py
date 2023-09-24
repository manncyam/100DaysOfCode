from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECOND_IN_MS = 1000
WORK_IN_SECOND = WORK_MIN * 60
SHORT_BREAK_IN_SECOND = SHORT_BREAK_MIN * 60
LONG_BREAK_IN_SECOND = LONG_BREAK_MIN * 60

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    canvas.itemconfig(canvas_timer, text="00:00")
    checked_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global reset
    reset = False

    if reps % 2 == 0:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_IN_SECOND)
    elif reps % 7 == 0:
        title_label.config(text="LBreak", fg=RED)
        countdown(LONG_BREAK_IN_SECOND)
    else:
        title_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_IN_SECOND)
    
    reps = (reps + 1) % 8

    checked_mark = ""
    for _ in range(reps // 2):
        checked_mark = f"{checked_mark}✔"
    checked_label.config(text=checked_mark)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min = math.floor(count / 60)
    sec = count % 60
    min = f"{min}" if min > 9 else f"0{min}"
    sec = f"{sec}" if sec > 9 else f"0{sec}"
    canvas.itemconfig(canvas_timer, text=f"{min}:{sec}")
    
    if count > 0 and not reset:
        global timer
        timer = window.after(SECOND_IN_MS, countdown, count - 1)
    elif sec == "00" and min == "00":        
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

title_label = Label(text="Timer", width=7, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

tomato = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
canvas_timer = canvas.create_text(105, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.config(bg=YELLOW)

canvas.grid(row=1, column=1)

start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(row=2, column=0)

checked_label = Label(text="", fg=GREEN, bg=YELLOW)
checked_label.grid(row=3, column=1)

reset_btn = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(row=2, column=2)

window.mainloop()