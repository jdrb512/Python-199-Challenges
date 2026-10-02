# Monday Motivation Project
import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

# O usas la librería python-dotenv
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("Day32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="josedrb1024@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# import smtplib

# my_email = "joserbd512@gmail.com"
# password = "xjqzvdgbhezrvfra"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="josedrb1024@gmail.com",
#         msg="Subject:Hello\n\nHello",
#     )

# import datetime as dt

# now = dt.datetime.now()
# print(now)
