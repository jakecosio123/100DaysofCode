import requests
from datetime import datetime
import smtplib
from time import sleep

# account I just set up and plan to never use
# in prod env this would be saved in some sort of secrets manager
MY_EMAIL = "jcosiomail@gmail.com"
MY_PASSWORD = "ussvuqgxmqzkoqwq"
MY_LAT = 33.197960
MY_LONG = -96.615021

scanning = True


def iss_is_in_view():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_dark_out():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False


while scanning:
    sleep(60)
    if iss_is_in_view() and is_dark_out():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                to_addrs="jakecosio123@gmail.com",
                from_addr=MY_EMAIL,
                msg=f"Subject:ISS is in view\n\nAssuming that tonight is clear, the ISS should be in view. Go see"
                    f"if you can find it!"
            )
