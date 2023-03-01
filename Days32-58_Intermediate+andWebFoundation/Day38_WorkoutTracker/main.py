import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

nutritionix_body = {
    "query": input("What exercise did you do? "),
    "gender": "male",
    "weight_kg": 111,
    "height_cm": 178,
    "age": "33"
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         headers=nutritionix_headers,
                         json=nutritionix_body)
exercise_data = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheety_headers = {
    "content-type": "application/json",
    "Authorization": SHEETY_TOKEN,
}

for item in exercise_data["exercises"]:
    exercise = item["name"]
    duration = item["duration_min"]
    calories = item["nf_calories"]
    workout = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }
    requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=workout)
