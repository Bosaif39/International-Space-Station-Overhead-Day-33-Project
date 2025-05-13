
# **ISS Overhead Notification Sender**

## **Overview:**
This is the Day 33 project from the 100 Days of Code: The Complete Python Pro Bootcamp.

This is a Python-based script that checks if the International Space Station (ISS) is overhead and if it is night time in your location. If both conditions are met, it sends an email notification to let you know that the ISS is visible in the sky above you.

This project makes use of the **Open Notify API** to track the current location of the ISS and the **Sunrise-Sunset API** to determine whether it's night in your area.

## **How It Works:**

1. The app regularly checks the position of the ISS using the **Open Notify API**.
2. It checks if the ISS is within a 5-degree range of your geographical coordinates (latitude and longitude).
3. The program also checks whether it is night time in your location by querying the **Sunrise-Sunset API**.
4. If the ISS is overhead and it’s night time, the program sends you an email notification, letting you know that the ISS is visible in the sky.
5. The script runs continuously in a loop, checking every minute.

## **Features:**

* **ISS Location Tracking**
* **Nighttime Detection**
* **Email Notification** 
* **Customizable Email Credentials** 


## **Instructions:**

1. **Setup Email**:

   * Replace `MY_EMAIL` and `MY_PASSWORD` with your actual email credentials.
   * Make sure to allow access to less secure apps or use an **App Password** if using services like Gmail.

2. **Location Configuration**:

   * Replace `MY_LAT` and `MY_LONG` with your geographical coordinates (latitude and longitude).
   * These values determine the location for checking if the ISS is overhead.


## **Requirements:**

* **Python 3.x**
* `requests`: For making HTTP requests to the APIs.
* `smtplib`: For sending emails via SMTP.
* `datetime`: For getting the current time and checking if it is night.
* `time`: For implementing a delay between checks.

