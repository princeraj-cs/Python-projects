from tkinter import*
from tkinter import messagebox
from pyperclip import copy
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_num

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_data = website_entry.get()
    email_data = email_entry.get()
    pass_data = pass_entry.get()

    if len(website_data)== 0 or len(email_data) == 0 or len(pass_data) == 0:
        pop_up = messagebox.showinfo(title="Warning", message="Don't leave something empty")
    else:
        want_to_save = messagebox.askokcancel(title=website_data, message=f"These are the details entered:"
                                                           f"\nEmail: {email_data}"
                                                           f"\nPassword: {pass_data}"
                                                           f"\nIs it okay to save?")
        if want_to_save:
            with open("password.txt", "a") as f:
                f.write(f"\n{website_data} | {email_data} | {pass_data}")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0, sticky="w")
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0, sticky="w")
email_entry = Entry(width=35)
email_entry.insert(0, "xyz@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

pass_text = Label(text="Password:")
pass_text.grid(row=3, column=0, sticky="w")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="ew")

gen_pass_button = Button(text="Generate Password", command=gen_pass)
gen_pass_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)


window.mainloop()


