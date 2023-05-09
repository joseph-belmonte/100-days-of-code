""" Automated Birthday Wisher"""

import os
import smtplib
import datetime as dt
import random
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
# future: use protonmail
MY_EMAIL = os.getenv("MY_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
PASSWORD = os.getenv("PASSWORD")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
# create a birthday dictionary
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, encoding="utf-8") as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# select a random quote from quotes.txt
with open("quotes.txt", encoding="utf-8") as file:
    quotes = file.readlines()
    random_quote = random.choice(quotes)

# send in the email with the quote
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)  # type: ignore
    connection.sendmail(
        from_addr=MY_EMAIL,  # type: ignore
        to_addrs=TO_EMAIL,  # type: ignore
        msg=f"Subject:Motivational Quote\n\n{random_quote}",
    )

