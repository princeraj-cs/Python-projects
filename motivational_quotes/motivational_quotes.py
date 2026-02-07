import smtplib
import datetime as dt
from random import choice

with open("quotes.txt") as file:
    quote = file.readlines()
    random_quote = choice(quote)

my_email = "EMAIL_ID"
"""There is no need of the main email if password you will have to generate a app password from you google account settings"""
password = "APP_PASSWORD" 

now = dt.datetime.now()
day_of_week = now.weekday() + 1

if day_of_week == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="RECIVER_EMAIL",
                            msg=f"Subject:MOTIVATIONAL QUOTE\n\n{random_quote}"
                            )