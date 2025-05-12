
# **ISS Overhead Notification Sender**

## **Overview:**

This is a Python-based script that checks if the International Space Station (ISS) is overhead and if it is night time in your location. If both conditions are met, it sends an email notification to let you know that the ISS is visible in the sky above you.

This project makes use of the **Open Notify API** to track the current location of the ISS and the **Sunrise-Sunset API** to determine whether it's night in your area.

## **How It Works:**

1. The app regularly checks the position of the ISS using the **Open Notify API**.
2. It checks if the ISS is within a 5-degree range of your geographical coordinates (latitude and longitude).
3. The program also checks whether it is night time in your location by querying the **Sunrise-Sunset API**.
4. If the ISS is overhead and it’s night time, the program sends you an email notification, letting you know that the ISS is visible in the sky.
5. The script runs continuously in a loop, checking every minute.

## **Features:**

* **ISS Location Tracking**: Checks if the ISS is overhead within a defined 5-degree range.
* **Nighttime Detection**: Verifies if it is night in your location based on sunrise and sunset times.
* **Email Notification**: Sends an email notification when both conditions are true.
* **Customizable Email Credentials**: Easily configure email settings for different email providers.

## **Requirements:**

* **Python 3.x**
* **requests**: For making HTTP requests to the APIs.
* **smtplib**: For sending emails via SMTP.
* **datetime**: For getting the current time and checking if it is night.
* **time**: For implementing a delay between checks.

## **File Structure:**

* **Main Python Script**: The Python file that runs the script.

  * Make sure to replace placeholders like `MY_EMAIL`, `MY_PASSWORD`, and SMTP server address.
  * The script continuously checks for the ISS and sends an email if the conditions are met.

## **Instructions:**

1. **Setup Email**:

   * Replace `MY_EMAIL` and `MY_PASSWORD` with your actual email credentials.
   * Make sure to allow access to less secure apps or use an **App Password** if using services like Gmail.
   * Specify your email provider's SMTP address in place of `__YOUR_SMTP_ADDRESS_HERE___`.

2. **Location Configuration**:

   * Replace `MY_LAT` and `MY_LONG` with your geographical coordinates (latitude and longitude).
   * These values determine the location for checking if the ISS is overhead.

3. **Run the Script**:

   * Run the Python script, and it will continuously monitor the ISS position and check if it’s night time.
   * If the ISS is overhead and it’s night, you’ll receive an email notification with the message: `The ISS is above you in the sky.`

## **How to Run:**

1. Ensure you have Python 3.x installed.
2. Install the required libraries by running:

   ```bash
   pip install requests
   ```
3. Update the script with your email credentials and geographical location.
4. Run the Python script:

   ```bash
   python iss_notification.py
   ```

