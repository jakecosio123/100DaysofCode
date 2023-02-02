from tkinter import *


def button_clicked():
    my_label.config(text=screen_input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

# button

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Click Me2")
button2.grid(column=2, row=0)

# entry

screen_input = Entry(width=10)
# screen_input.pack()
screen_input.grid(column=3, row=2)

window.mainloop()
