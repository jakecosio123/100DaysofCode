class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, depart_date,
                 return_date, nights_in_dest, link):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.depart_date = depart_date
        self.return_date = return_date
        self.nights_in_dest = nights_in_dest
        self.link = link
