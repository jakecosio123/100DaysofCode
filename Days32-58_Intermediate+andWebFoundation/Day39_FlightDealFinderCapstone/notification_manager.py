import os
import smtplib
from email.mime.text import MIMEText


class NotificationManager:

    def __init__(self):
        self.email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("MY_PASSWORD")
        self.message = "Hello,<br><br> We have found the following flight deals for you today:<br><br>"

    def send_email(self):

        message = MIMEText(self.message, "html")
        message["Subject"] = "Flight Deals"
        message["From"] = self.email
        message["To"] = "jakecosio123@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                to_addrs="jakecosio123@gmail.com",
                from_addr=self.email,
                msg=message.as_string()
            )

    def format_message(self, destination, price, nights_in_dest, depart_date, return_date, link):
        self.message += f'<strong>Destination: {destination}</strong>    Price: ${price}<br>' \
                  f'Nights in destination: {nights_in_dest}<br>' \
                  f'Date of departure: {depart_date} <br>' \
                  f'Date of return: {return_date}<br>' \
                  f'Link to book: <a href="{link}">Click Here</a><br><br>'
