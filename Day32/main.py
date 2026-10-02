# Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "joserbd512@gmail.com"
MY_PASSWORD = "xjqzvdgbhezrvfra"

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
