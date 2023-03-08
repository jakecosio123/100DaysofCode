import os
import requests
from flight_data import FlightData
from datetime import datetime
from dateutil.relativedelta import *


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.response = None
        self.parameters = None
        self.tequila_apikey = os.environ.get("TEQUILA_APIKEY")
        self.headers = {
            "apikey": self.tequila_apikey,
            "accept": "application/json",
        }
        self.from_date = datetime.now()
        self.to_date = self.from_date + relativedelta(months=+6)
        self.from_date = self.from_date.strftime("%d/%m/%Y")
        self.to_date = self.to_date.strftime("%d/%m/%Y")

    def get_iata_code(self, city):
        self.parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "active_only": "true",
        }
        self.response = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                     headers=self.headers,
                                     params=self.parameters)
        data = self.response.json()
        return data["locations"][0]["code"]

    def search_flights(self, iata_codes):

        self.parameters = {
            "fly_from": "city:DFW",
            "fly_to": f"{iata_codes}",
            "date_from": self.from_date,
            "date_to": self.to_date,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "adults": 1,
            "one_for_city": 1,
            "curr": "USD",
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search",
                                headers=self.headers,
                                params=self.parameters)
        try:
            data = response.json()
        except IndexError:
            print(f"No flights found")
            return None
        try:
            flight_data = FlightData(
                price=data["data"][0]["price"],
                origin_city=data["data"][0]["cityFrom"],
                origin_airport=data["data"][0]["flyFrom"],
                destination_city=data["data"][0]["cityTo"],
                destination_airport=data["data"][0]["flyTo"],
                depart_date=data["data"][0]["route"][0]["local_departure"].split("T")[0],
                return_date=data["data"][0]["route"][-1]["local_departure"].split("T")[0],
                nights_in_dest=data["data"][0]["nightsInDest"],
                link=data["data"][0]["deep_link"]
            )
        except IndexError:
            flight_data = FlightData(
                price=9999999,
                origin_city=0,
                origin_airport=0,
                destination_city=0,
                destination_airport=0,
                depart_date=0,
                return_date=0,
                nights_in_dest=0,
                link=0
            )
        else:
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            print(f"Depart: {flight_data.depart_date}, Return: {flight_data.return_date}")
            print(f"Nights in destination: {flight_data.nights_in_dest}")
            print(flight_data.link)
        finally:
            return flight_data
