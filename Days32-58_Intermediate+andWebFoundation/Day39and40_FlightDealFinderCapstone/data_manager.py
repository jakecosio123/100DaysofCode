import gspread
from flight_search import FlightSearch


class DataManager:

    def __init__(self):
        self.gc = gspread.service_account()
        self.sh = self.gc.open("Flight Deals")
        self.ws = self.sh.get_worksheet(0)
        self.ws_two = self.sh.get_worksheet(1)
        self.data = self.ws.get_all_values()
        self.data_ws_two = self.ws_two.get_all_values()
        self.num_of_rows = len(self.data)
        self.flight_search = FlightSearch()

    def update_iata_codes(self):
        index = 0
        for item in self.data:
            index += 1
            if item[1] == "":
                iata_code = self.flight_search.get_iata_code(item[0])
                self.ws.update(f"B{index}", iata_code)
        self.gc = gspread.service_account()
        self.sh = self.gc.open("Flight Deals")
        self.ws = self.sh.get_worksheet(0)
        self.data = self.ws.get_all_values()

    def update_sheet(self, row_number, search_date, price, nights_in_dest, depart_date, return_date, link):
        self.ws.update(f"D{row_number}", search_date)
        self.ws.update(f"E{row_number}", price)
        self.ws.update(f"F{row_number}", nights_in_dest)
        self.ws.update(f"G{row_number}", depart_date)
        self.ws.update(f"H{row_number}", return_date)
        self.ws.update_cell(col="9", row=f"{row_number}", value=f'=HYPERLINK("{link}","Kiwi Link")')

    def get_emails(self):
        email_list = []
        num_of_users = len(self.data_ws_two)
        for num in range(1, num_of_users):
            email_list.append(self.data_ws_two[num][2])
        return email_list
