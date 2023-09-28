##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import os
import random
import smtplib
from email.message import EmailMessage

today = dt.datetime.now()

df = pd.read_csv("birthdays.csv")

bd_series_temp = df[df.month == today.month]
bd_series = bd_series_temp[bd_series_temp.day == today.day]

if len(bd_series) > 0:
    recipients = []
    for index, row in bd_series.iterrows():
        recipients.append({"name": row["name"], "email": row["email"]})
    if len(recipients) > 0:
        path = "letter_templates"
        dir_list = os.listdir(path)

        sender = "cblue77@gmail.com"
        password = "gtct rluv ktqg iwvz"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            for recipient in recipients:
                letter_template = f"{path}/{random.choice(dir_list)}"
                with open(letter_template, mode="r") as infile:
                    letter = infile.read()

                specific_letter = letter.replace("[NAME]", recipient["name"])
                #print(recipient["email"],specific_letter)
                msg = EmailMessage()
                msg.set_content(specific_letter)
                msg['Subject'] = f"{recipient['name']} Happy Birthday!"
                msg['From'] = sender
                msg['To'] = recipient["email"]

                connection.send_message(msg)
                #connection.sendmail(from_addr=sender, to_addrs=recipient["email"], 
                #                    msg=f"Subject: Happy Birthday\n\n{specific_letter}")