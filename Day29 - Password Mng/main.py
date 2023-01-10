from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generate():
    pass_ent.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_ent.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_ent.get()
    email = email_ent.get()
    password = pass_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered:\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_ent.delete(0, END)
                pass_ent.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_ent.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    except KeyError:
        messagebox.showerror(title="Error", message="No Website Found!")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)

pass_lbl = Label(text="Password:")
pass_lbl.grid(column=0, row=3)

website_ent = Entry(width=41)
website_ent.grid(column=1, row=1)
website_ent.focus()

email_ent = Entry(width=60)
email_ent.grid(column=1, row=2, columnspan=2)
email_ent.insert(0, "myemail@gmail.com")

pass_ent = Entry(width=41)
pass_ent.grid(column=1, row=3)

pass_btn = Button(text="Generate Password", command=pass_generate)
pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=51, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(column=2, row=1)

window.mainloop()
