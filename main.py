from tkinter import Tk, Button, Label, Entry


def convert_miles_km():
    miles = int(text_input.get()) * 1.6
    km_value.config(text=round(miles))
    return round(miles)


# Window Configuration
window = Tk()
window.title("Miles to Kilometers")
window.config(width=300, height=200, padx=20, pady=20)

# Entry Text Box Configuration
text_input = Entry()
text_input.config(width=10)
text_input.grid(column=1, row=0, padx=5, pady=5)

# Labels Configuration
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=5, pady=5)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1, padx=5, pady=5)

km_value = Label(text="0")
km_value.grid(column=1, row=1, padx=5, pady=5)

km_label = Label(text="KMs")
km_label.grid(column=2, row=1, padx=5, pady=5)

# Button Configuration
cal_button = Button(text="Calculate", command=convert_miles_km)
cal_button.grid(column=1, row=2, padx=5, pady=5)

window.mainloop()
