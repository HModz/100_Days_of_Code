from tkinter import *


def button_clicked():
    mile = input.get()
    km = int(mile) * 1.6
    output.config(text=km)


window = Tk()
window.title("Mile to Kilometers Converter")
window.maxsize(width=500, height=300)
window.config(padx=10, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=30)
input.grid(column=1, row=0)

window.mainloop()
