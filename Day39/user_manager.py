""" this script adds a user to the google sheet """
import os
import requests
from dotenv import load_dotenv

load_dotenv()

ENV_SHEETY_USERS_ENDPOINT = os.environ["ENV_SHEETY_USERS_ENDPOINT"]

sheety_header = {"Authorization": os.environ["ENV_SHEETY_HEADER"]}


def post_new_user(first_name, last_name, email):
    """adds a new user to the google sheet, users tab"""

    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    response = requests.post(
        url=ENV_SHEETY_USERS_ENDPOINT, json=user_data, headers=sheety_header, timeout=5
    )
    response.raise_for_status()
    print(response.status_code)
    print(response.text)
