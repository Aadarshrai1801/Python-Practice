# Password Manager using Python

from tkinter import *

# PASSWORD GENERATOR 

# SAVE PASSWORD 

# UI SETUP

    # Window
    
window = Tk()
window.title("Password Manager")
window.minsize(350, 350)

    # Canvas

canvas = Canvas(width=200, height=224, bg = window.cget("bg"))  
img = PhotoImage(file = "29thDay/Logo.png")
canvas.create_image(100, 100, image = img)
canvas.pack(padx = 20, pady = 65)

print("Hello World")

window.mainloop()