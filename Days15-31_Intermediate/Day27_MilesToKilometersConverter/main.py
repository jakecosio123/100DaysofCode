from tkinter import *


def calculate():
    mi = float(input_miles.get())
    km = round(mi * 1.609344, 1)
    output_km.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=70, pady=25)

input_miles = Entry()
input_miles.grid(column=1, row=0)
input_miles.config(width=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

output_km = Label()
output_km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()
