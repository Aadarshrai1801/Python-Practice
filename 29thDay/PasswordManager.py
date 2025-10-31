# Password Manager using Python

from tkinter import *

from tkinter import messagebox

import random

import pyperclip

import json

# PASSWORD GENERATOR 

def generate_password() :

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letters + password_symbols + password_numbers

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  
  pyperclip.copy(password)  

# SAVE PASSWORD 

def save_password():
    
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0 :
        messagebox.showinfo(title = "Error", message = "You have left any field empty.")
    
    else :
        try :
            with open("29thDay/Passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError :
            with open("29thDay/Passwords.json", "w") as data_file :
                json.dump(new_data, data_file, indent = 4)        
        else :    
            # Updating old data with new data
            data.update(new_data)
            
            with open("29thDay/Passwords.json", "w") as data_file :
                json.dump(data, data_file, indent = 4)
                 
        finally :
            website_entry.delete(0, END)
            password_entry.delete(0, END)          
                
# LOAD PASSWORDS

def load_pass() :
    website = website_entry.get()
    try :
        with open("29thDay/Passwords.json", "r") as file :
            data1 = json.load(file)
    except FileNotFoundError :
        messagebox.showinfo(title = "Error", message = "No Data File Found.")
    else:
        if website in data1 :
            messagebox.showinfo(
                title=website,
                message = f"Email: {data1[website]['email']}\nPassword: {data1[website]['password']}"
            )
        else :
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# UI SETUP

    # Window
    
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

    # Canvas

canvas = Canvas(width = 200, height = 200, bg = window.cget("bg"))  
img = PhotoImage(file = "29thDay/Logo.png")
canvas.create_image(100, 100, image = img)
canvas.grid(row = 0, column = 1)

    # Label
    
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0) 

username_label = Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)  

password_label = Label(text = "Password:") 
password_label.grid(row = 3, column = 0)

    # Entries
    
website_entry = Entry(width = 30)  
website_entry.grid(row = 1, column = 1)
website_entry.focus()

username_entry = Entry(width = 35)
username_entry.grid(row = 2, column = 1, columnspan = 2)
username_entry.insert(END, "aadarshrai1801@gmail.com") 

password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)

    # Button
    
generate_button = Button(text = "Generate Password", command = generate_password)
generate_button.grid(row = 3, column = 2)    
    
add_button = Button(text = "Add", width = 36, command = save_password)  
add_button.grid(row = 4, column = 1, columnspan = 2)  

search_button = Button(text = "Search", width = 15, command = load_pass)
search_button.grid(row = 1, column = 2)

window.mainloop()