import os
import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"


from dotenv import load_dotenv

load_dotenv()

pixela_token = os.getenv("PIXELA_TOKEN")

user_params = {
    "token": pixela_token,
    "username": "joebel",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
TODAY = dt.datetime.now().date().strftime("%Y%m%d")

# create the user
# response = requests.post(url=pixela_endpoint, json=user_params, timeout=5)
# print(response.text)

# create a graph
graph_endpoint = f"{pixela_endpoint}/joebel/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, timeout=5, headers=headers
# )
# print(response.text)

headers = {
    "X-USER-TOKEN": pixela_token,
}

pixel_creation_endpoint = f"{pixela_endpoint}/joebel/graphs/graph1"

pixel_data = {
    "date": TODAY,
    "quantity": "3.5",
}

# add a pixel to the graph
response = requests.post(
    url=pixel_creation_endpoint, json=pixel_data, timeout=5, headers=headers
)
print(response.text)

# put and delete requests are also available
