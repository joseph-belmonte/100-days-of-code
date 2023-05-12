""" This class is responsible for talking to the Flight Search API.
    It contains the methods: get_destination_code and check_flights.
"""
import os
import requests
from flight_data import FlightData
from dotenv import load_dotenv


load_dotenv()

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ["ENV_TEQUILA_API_KEY"]


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def get_destination_code(self, city_name):
        """Takes in a city name and returns the IATA code"""
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(
            url=location_endpoint, headers=headers, params=query, timeout=5
        )
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        """Checks for flights from origin to destination within the time range"""
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "USD",
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
            timeout=5,
        )
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
