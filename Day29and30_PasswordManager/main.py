from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}\n"
                                                      f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1, sticky="E")
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2, sticky="E")
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3, sticky="E")

web_entry = Entry()
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW", pady=3)
web_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=3)
username_entry.insert(0, "example_autofill_email@gmail.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, columnspan=2, sticky="EW", pady=3)

pass_gen_btn = Button(text="Generate Password", command=password_generator)
pass_gen_btn.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW", pady=3)


window.mainloop()
