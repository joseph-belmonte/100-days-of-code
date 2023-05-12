"""weather app"""
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

from dotenv import load_dotenv

trial_number = "+18332502361"

load_dotenv()
# API_KEY = os.getenv("API_KEY")
API_KEY = "69f04e4613056b159c2761a9d9e664d2"  # angela's api key
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
my_cell = os.getenv("MY_CELL")


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"


weather_params = {
    "lat": 35.2423,
    "lon": -87.33,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params, timeout=5)
response.raise_for_status()
weather_data = response.json()
# CHECK HOURLY FOR THE NEXT 12 HOURS
hourly_weather_data = weather_data["hourly"][:12]
for hour_data in hourly_weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        print("Bring an umbrella")
        break


if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella! ☔️",
        from_=trial_number,
        to=my_cell,  # type: ignore
    )
    print(message.status)
    print(message.sid)
