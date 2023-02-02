import smtplib
import random
import pandas
import datetime as dt

# account I just set up and plan to never use
# in prod env this would be saved in some sort of secrets manager
MY_EMAIL = "jcosiomail@gmail.com"
MY_PASSWORD = "ussvuqgxmqzkoqwq"

# open birthday file and save to list for future reference
b_days = pandas.read_csv("birthdays.csv")
b_day_list = b_days.to_dict("records")

# choose the letter that we will send
letter_choice = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"
print(letter_choice)
with open(letter_choice) as letter:
    message = letter.read()

# set date variables to check against
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# iterate through all bdays in b_day_list to check if any of the bdays are today
for b_day in b_day_list:
    if b_day["day"] == current_day and b_day["month"] == current_month:

        # replace [NAME] with the name of the person whose bday it is
        formatted_message = message.replace("[NAME]", b_day["name"])

        # start connection to gmail mail server, secure it, login, then send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                to_addrs=b_day["email"],
                from_addr=MY_EMAIL,
                msg=f"Subject:Happy Birthday\n\n{formatted_message}"
            )
