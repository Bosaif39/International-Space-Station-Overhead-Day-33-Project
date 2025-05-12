import requests  
from datetime import datetime  
import smtplib  
import time  

# Email credentials and location (replace these with your actual details)
MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351  # Latitude of your location (e.g., London)
MY_LONG = -0.127758  # Longitude of your location (e.g., London)

# Function to check if the ISS is currently overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  
    data = response.json()  

    # Extracting the ISS latitude and longitude from the response
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # This is the "overhead" range to check if the ISS is nearby
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True  
 

def is_night():
    parameters = {
        "lat": MY_LAT,  
        "lng": MY_LONG,  
        "formatted": 0,  
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  
    data = response.json()  

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Checking if the current time is during nighttime (before sunrise or after sunset)
    if time_now >= sunset or time_now <= sunrise:
        return True  
    

# Infinite loop to check every minute if the ISS is overhead and it's nighttime
while True:
    time.sleep(60)  
    if is_iss_overhead() and is_night():  
        
        connection = smtplib.SMTP("smtp.gmail.com")  
        connection.starttls()  # Start TLS encryption for secure connection
        connection.login(MY_EMAIL, MY_PASSWORD)  
        connection.sendmail(
            from_addr=MY_EMAIL,  
            to_addrs=MY_EMAIL,  
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."  
        )
