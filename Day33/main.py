from datetime import datetime
import requests
import time

MY_LAT = 40.4406  # Your latitude
MY_LONG = 79.9959  # Your longitude
LOCAL_UTC_OFFSET = 4


def utc_to_local(utc_hour):
    """Converts UTC time to local time."""
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def is_iss_overhead():
    """Returns True if the ISS is close to my current position (within 5 degrees of my position).
    and it is currently dark"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=5)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        iss_latitude > MY_LAT - 5
        and iss_latitude < MY_LAT + 5
        and iss_longitude > MY_LONG - 5
        and iss_longitude < MY_LONG + 5
    ):
        return True
    return False


def is_dark():
    """Returns True if it is currently dark, False if it is light."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters, timeout=5
    )
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    lt_sunrise = utc_to_local(sunrise)
    lt_sunset = utc_to_local(sunset)

    time_now = datetime.now()

    if time_now.hour >= lt_sunset or time_now.hour <= lt_sunrise:
        return True
    return False


while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(120)
    # If the ISS is close to my current position
    # and it is currently dark
    if is_iss_overhead() and is_dark():
        # Then send me an email to tell me to look up.
        print("Look up!")
    else:
        print("Nope.")
