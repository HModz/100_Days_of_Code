import datetime as dt
import pandas
import random
import smtplib

MYEMAIL = ""
PASSWORD = ""

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.items}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MYEMAIL, PASSWORD)
        connection.sendmail(from_addr=MYEMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{content}")
