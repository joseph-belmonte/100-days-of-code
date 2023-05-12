"""This class is responsible for talking to the Google Sheet. It contains the methods:
get_destination_data and update_destination_codes."""
import os
import requests

from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]

sheety_header = {"Authorization": os.environ["ENV_SHEETY_HEADER"]}


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Read data from the google sheet"""
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT, timeout=5, headers=sheety_header
        )
        response.raise_for_status()
        data = response.json()

        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update IATA codes in the google sheet"""
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                timeout=5,
                headers=sheety_header,
            )
            print(response.text)
