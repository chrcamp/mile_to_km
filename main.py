from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles")
equal_label = Label(text="is equal to")
km_label = Label(text="Km")
results_label = Label(text=0)


# Buttons
def convert_to_km():
    user_input = float(entry_box.get())
    result = round(user_input * 1.60934, 2)
    results_label.config(text=result)


calc_button = Button(text="Calculate", command=convert_to_km)


# Entry
entry_box = Entry(width=10)
entry_box.insert(END, string="0")


# Layout
entry_box.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
results_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calc_button.grid(column=1, row=2)

window.mainloop()
