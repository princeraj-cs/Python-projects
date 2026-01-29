from tkinter import *

window = Tk()
window.title('Mile to km converter')
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

FONT = font=("Arial", 12, "bold")

def miles_to_km():
    mile = float(miles_input.get())
    km = mile * 1.609
    km_calc.config(text=f"{km}")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

text1 = Label(text="is equals to")
text1.grid(column=0, row=1)

km_calc = Label(text=0)
km_calc.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=3)



window.mainloop()