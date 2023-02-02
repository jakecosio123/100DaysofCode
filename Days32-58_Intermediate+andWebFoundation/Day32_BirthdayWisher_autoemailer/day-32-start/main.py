import smtplib
import datetime as dt
import random

MY_EMAIL = "jcosiomail@gmail.com"
MY_PASSWORD = "ussvuqgxmqzkoqwq"

now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()

#
# date_of_birth = dt.datetime(year=1990, month=1, day=15, hour=17, minute=7)
# print(date_of_birth)

if day_of_week == 3:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jakecosio123@gmail.com",
            msg=f"Subject:Thursday Quote\n\n{quotes[random.choice(quotes)]}"
        )