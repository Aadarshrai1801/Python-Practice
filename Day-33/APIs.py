# Application Programming Interfaces(APIs) in Python

import requests
import datetime as dt

# Day 33-1-Exercise

from tkinter import *

def get_quote():
    response = requests.get(url = "https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text = f"{data['quote']}")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="33rdDay/Background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text = f"Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="33rdDay\Kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()

# Day 33-2-Exercise

MY_LAT = 31.633980
MY_LNG = 74.872261 

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters) 

response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(dt.datetime.now().hour)