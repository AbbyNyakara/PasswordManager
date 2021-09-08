from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
# NB: The pyperclip module is used to copy the password to the clipboard
# ------------------------------ GENERATE THE PASSWORD ---------------------------------
# Create a list

def generate_password():
    all_letters = list(string.ascii_letters)
    all_numbers = list(string.digits)
    all_symbols = list(string.punctuation)

    nr_letters = random.randint(6, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    letters_list = [random.choice(all_letters)for letter in range(nr_letters)]
    numbers_list = [random.choice(all_numbers) for num in range(nr_numbers)]
    symbols_list = [random.choice(all_symbols) for char in range(nr_symbols)]
    password = letters_list + numbers_list + symbols_list
    random.shuffle(password)   # Note that this is still a list
    password = "".join(password)
    # print(password)

    # Insert the generated password into the password entry
    password_entry.insert(0, password)
    pyperclip.copy(text=password)  # The text to be copied to the clipboard

# TODO - Create a password manager that will take the password and store it in a text file
# -------------------- SAVE THE PASSWORD TO TEXT FILE ONCE THE USER PRESSES ADD BUTTON --------------

def save():
    # Get all the info from the entries
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Make sure that the user has the inputs the inputs cannot be empty.
    if len(web) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="You still have some empty fields ")

    else:
        # Use a pop up message box to confirm whether the user has the correct info.
        choice = messagebox.askyesno(title=web, message=f"Your email is: {email} \n"
                                                        f"Your password is: {password} for the {web} website.\n"
                                                        f"Would you like to save?")
        if choice is True:
            # Open the text file and append the email, password and website info
            with open("info.txt", "a") as data_file:
                data_file.write(f"{web} | {email} | {password} \n")
                # Once you've written to the file, delete the entries so show the action is completed
                # Note: It is the entries getting deleted. Not entries.get()
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ----------------------------------------- CREATE THE UI OF THE PASSWORD MANAGER---------------------------------
# Steps
# Set up the window

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Import the image
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Create the Labels and the entries and the buttons
# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "abbynyakara@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
