from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

mile_entry = Entry(width=20)
mile_entry.grid(row=0, column=1)
mile_entry.insert(END, string="0")
mile_entry.focus()
#mile_entry.config(padx=10, pady=10)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)
mile_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)
equal_label.config(padx=10, pady=10)

in_km_label = Label(text="0")
in_km_label.grid(row=1, column=1)
in_km_label.config(padx=10, pady=10)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

def calculate():
    if mile_entry.get() != "":
        mile = float(mile_entry.get())
        result = round(mile * 1.609, 2)
        in_km_label.config(text=f"{result}")

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=10, pady=10)


window.mainloop()