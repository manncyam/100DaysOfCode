import requests
import datetime as dt
import os

TOKEN = os.getenv("pixela_token")
USERNAME = os.getenv("pixela_username")
GRAPH_ID = "first-graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_URL_CREATE_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_URL_UPDATE_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

parameters_graph = {
    "id": GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}

now = dt.datetime.now()
distance = input("How many kilometer did you cycle today? ")

parameters_value = {
    "date": now.strftime("%Y%m%d"),
    "quantity": distance
}

header_parameters = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=PIXELA_URL_UPDATE_GRAPH, json=parameters_value, headers=header_parameters)
#response.raise_for_status()
print(response.text)