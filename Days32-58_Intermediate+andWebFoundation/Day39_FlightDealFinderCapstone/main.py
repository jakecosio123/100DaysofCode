# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
flights = ["placeholder"]
deals = []
message = "Hello,\n\n We have found the following flight deals for you today:\n\n"

data_manager.update_iata_codes()

for num in range(1, data_manager.num_of_rows):
    flights.append(flight_search.search_flights(data_manager.data[num][1]))

print(flights)

# for item in sheet_data:
#     iata_code = item["iataCode"]
#     flight_info = flight_search.search_flights(iata_code)
#     flights.append(flight_info)
#
for num in range(1, data_manager.num_of_rows):
    if (int(flights[num].price) <= int(data_manager.data[num][2])
        and datetime.now().strftime("%m/%d/%Y") != data_manager.data[num][3]) \
            or (datetime.now().strftime("%m/%d/%Y") == data_manager.data[num][3]
                and int(flights[num].price) < int(data_manager.data[num][4])):
        data_manager.update_sheet(row_number=num + 1,
                                  search_date=datetime.now().strftime("%m/%d/%Y"),
                                  price=flights[num].price,
                                  nights_in_dest=flights[num].nights_in_dest,
                                  depart_date=flights[num].depart_date,
                                  return_date=flights[num].return_date,
                                  link=flights[num].link)
        deals.append(flights[num])

for deal in deals:
    notification_manager.format_message(destination=deal.destination_city,
                                        price=deal.price,
                                        nights_in_dest=deal.nights_in_dest,
                                        depart_date=deal.depart_date,
                                        return_date=deal.return_date,
                                        link=deal.link)

if notification_manager.message != "Hello,<br><br> We have found the following flight deals for you today:<br><br>":
    notification_manager.send_email()
    print("Sent email")
