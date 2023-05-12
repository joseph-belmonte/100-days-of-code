""" This class is responsible for sending notifications with the deal flight details. 
    It contains the NotificationManager class and send_email method.
"""
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

MY_EMAIL = os.getenv("ENV_MY_EMAIL")
PASSWORD = os.getenv("ENV_PASSWORD")
TO_EMAIL = os.getenv("ENV_TO_EMAIL")


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        pass

    def send_email(self, message):
        """Send Email notification"""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)  # type: ignore
            connection.sendmail(
                from_addr=MY_EMAIL,  # type: ignore
                to_addrs=TO_EMAIL,  # type: ignore
                msg=f"Subject:FLIGHT DEALS\n\n{message}",
            )
            # Prints if successfully sent.
            print("Email sent.")
