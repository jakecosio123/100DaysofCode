import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New Text")

# button


def button_clicked():
    my_label.config(text=screen_input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# entry

screen_input = tkinter.Entry(width=10)
screen_input.pack()
screen_input.get()

window.mainloop()
