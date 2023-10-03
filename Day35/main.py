import requests
import json
import os

OWM_API_URL = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat":33.745472,
    "lon":-117.867653,
    "appid":os.getenv("OWM_API_KEY")
}

response = requests.get(url=OWM_API_URL, params=parameters)
response.raise_for_status()
with open("data.json", mode="w") as of:
    data = response.json()
#     json.dump(data, of)

# with open("data.json", mode="r") as of:
#     data = json.load(of)

weather = data["list"][0]["weather"]
if 500 <= weather[0]["id"] <= 622:
    print("Please bring an umbrella with you!")
else:
    print("You are free to bring other stuff than an umbrella.")