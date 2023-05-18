"""Amazon Price Tracker"""
import os
import smtplib
import requests
import bs4


MY_EMAIL = os.environ["MY_EMAIL"]
TO_EMAIL = os.environ["TO_EMAIL"]
PASSWORD = os.environ["PASSWORD"]


# SET THE PRICE THRESHOLD
PRICE_THRESHOLD = 50

# get the product page
PRODUCT_URL = "https://camelcamelcamel.com/product/B0855R418S"
request_headers = {"User-Agent": "Defined"}
page = requests.get(
    PRODUCT_URL,
    headers=request_headers,
    timeout=5,
)

# parse the page
soup = bs4.BeautifulSoup(page.content, "html.parser")
prices = soup.find("table", {"class": "product_pane"}).getText()

# get the price
current_price_idx = prices.split("\n").index("Current") + 1
current_price = prices.split("\n")[current_price_idx]
current_price = float(current_price.replace("$", "").replace(",", ""))

# send an email if the price is below the threshold
if current_price < PRICE_THRESHOLD:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)  # type: ignore
        connection.sendmail(
            from_addr=MY_EMAIL,  # type: ignore
            to_addrs=TO_EMAIL,  # type: ignore
            msg=f"Subject: Amazon Price Alert!\n\nThe price of the product is now ${current_price}!\n{PRODUCT_URL}",
        )
