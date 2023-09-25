from tkinter import *
from tkinter import messagebox
import random
import pyperclip

INPUT_WIDTH = 50
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'\
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'\
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'\
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_rand(num, target):
    return [random.choice(target) for _ in range(0, num + 1)]

def generate_pass():
    num_letters = num_symbols = num_numbers = 6
    rand_letters = generate_rand(num_letters, letters)
    rand_symbols = generate_rand(num_symbols, symbols)
    rand_numbers = generate_rand(num_numbers, numbers)

    password_list = rand_letters + rand_symbols + rand_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opp", message="Please don't leave any fields emplty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save username: {username} and password: {password} for {website} website?")
        if is_ok:
            with open("data.txt", mode="a") as of:
                of.write(f"{website} | {username} | {password}\n")
            
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=500, height=400)
window.maxsize(width=500, height=400)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=INPUT_WIDTH)
website_input.grid(row=1, column=1, columnspan=2, pady=3, sticky="WE")
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=INPUT_WIDTH)
username_input.grid(row=2, column=1, columnspan=2, pady=3, sticky="WE")
username_input.insert(0, "m@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=30)
password_input.grid(row=3, column=1, pady=3, sticky="W")

gen_pass_btn = Button(text="Generate Password", command=generate_pass)
gen_pass_btn.grid(row=3, column=2, sticky="E")

add_btn = Button(text="Add", command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, pady=3, sticky="WE")






window.mainloop()