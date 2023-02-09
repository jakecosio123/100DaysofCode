import requests
from twilio.rest import Client
import os

MY_LAT = 33.197960
MY_LONG = -96.615021
MY_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


need_umbrella = False

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": MY_KEY,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][:12]

for item in hourly_data:
    if item["weather"][0]["id"] < 700 and not need_umbrella:
        need_umbrella = True
if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid="MG176ecd1c5b7005f70414d270ddce923f",
        body="It is going to rain today, bring and umbrella.☔",
        to="+14097671924",
    )

    print(message.status)
