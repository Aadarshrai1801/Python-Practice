# ISS Overhead Notifier program

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "aadarshrai1807@gmail.com"
PASSWORD = "gqtnowjjmllcaolj"

MY_LAT = 31.633980
MY_LNG = 74.872261

def is_overhead() :

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5) :
        return True
    
    return False

def is_night() :
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise :
        return True
    
    return False

while True :
    time.sleep(10)
    if is_overhead() and is_night() :
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs = "aadarshrai1801@yahoo.com",
                msg = "Subject: Look Up!\n\nThe ISS is above you right now. Go outside and look up!"
            )  
    else :
        print("Try again later!")        