"""stock news alert"""

import os
import smtplib
import datetime as dt
import requests
from dotenv import load_dotenv

from pandas.tseries.offsets import BDay

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_EMAIL = os.getenv("MY_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
PASSWORD = os.getenv("PASSWORD")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
TODAY = BDay(-1)._apply(dt.datetime.now()).to_pydatetime().strftime("%Y-%m-%d")  # type: ignore
YESTERDAY = BDay(-2)._apply(dt.datetime.now()).to_pydatetime().strftime("%Y-%m-%d")  # type: ignore

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

r = requests.get(url=STOCK_ENDPOINT, params=stock_params, timeout=5)
r.raise_for_status()
stock_data = r.json()
yesterday_closing_price = float(stock_data["Time Series (Daily)"][TODAY]["4. close"])
day_before_yesterday_closing_price = float(
    stock_data["Time Series (Daily)"][YESTERDAY]["4. close"]
)

price_change = abs(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
)
if price_change > 0.05 * day_before_yesterday_closing_price:
    UP_DOWN = "🔺"
else:
    UP_DOWN = "🔻"

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": "2023-05-01",
    "language": "en",
}

if price_change > 0.05 * day_before_yesterday_closing_price:
    print("Get News")

    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    news_data = requests.get(url=NEWS_ENDPOINT, params=news_params, timeout=5).json()
    news_articles = news_data["articles"][:3]

    # STEP 3: send an email with the first three articles titles and briefs
    message_body = f"{STOCK}: {UP_DOWN}{abs(price_change)}%\n"
    for article in news_articles:
        message_body += (
            f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
        )

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)  # type: ignore
        connection.sendmail(
            from_addr=MY_EMAIL,  # type: ignore
            to_addrs=TO_EMAIL,  # type: ignore
            msg=f"Subject:Stock News\n\n{message_body}",
        )
