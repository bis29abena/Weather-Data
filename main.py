import requests
from twilio.rest import Client
import os
import argparse

# Constructing the argparser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--lat", required=True, help="Input Latitude of your location", type=float)
ap.add_argument("--long", required=True, help="Input longitude of your location", type=float)
arg = vars(ap.parse_args())

# Open Weather map key
API_KEY = os.environ.get("OWM_API_KEY")
LAT = arg["lat"]
LONG = arg["long"]

# Twilio account key
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
request.raise_for_status()
weather_data = request.json()["hourly"]
weather_data_12_hours = weather_data[:12]

condition_code = False

for hours in weather_data_12_hours:
    weather = hours["weather"]
    id_ = (weather[0]["id"])
    if id_ < 700:
        condition_code = True

if condition_code:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="This Your Husband Bismark Please i have written some code to check the weather"
                 " And to prompt you if it will rain and if you see it meaning it will rain i love you"
                 " so much please remember that always ",
            from_="+18052593842",
            to="+233558345263"
        )
    print(message.status)
