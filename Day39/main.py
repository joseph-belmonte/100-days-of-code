""" This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
classes to achieve the program requirements. """
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import user_manager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "PIT"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    # print(flight)
    if flight and flight.price < destination["lowestPrice"]:
        notification_manager.send_email(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )


  

print("Welcome to Joe's Flight Club. \nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What is your email?\n")
    if email1.lower() == "q" or email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Confirm your email:\n")
    if email2.lower() == "q" or email2.lower() == "quit" or email2.lower() == "exit":
        exit()

print("You're in the club!")
user_manager.post_new_user(first_name, last_name, email1)
