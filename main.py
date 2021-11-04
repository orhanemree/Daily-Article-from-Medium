from bs4 import BeautifulSoup
from dotenv import dotenv_values
from datetime import datetime
import requests
import smtplib

# get page source code with requests
tag = "sports"
url = f"https://medium.com/tag/{tag}"
page = requests.get(url)

# parse source code with bs4
soup = BeautifulSoup(page.text, "html.parser")

# get last article about tag
articles = soup.select("#root > div > div.t.u > div > div > div.l.ao > div")[1].select(".l > div", limit=1)

# get last article's author name
author = articles[0].select("h4")[0].text

# get last article's title
title = articles[0].select("h2")[0].text

# get last article's description
description = articles[0].select("h3")[0].text

# try to get last article's image
try:
    image = articles[0].select("img")[4]
except IndexError:
    try:
        image = articles[0].select("img")[3]
    except IndexError:
        try:
            image = articles[0].select("img")[2]
        except IndexError:
            try:
                image = articles[0].select("img")[1]
            except IndexError:
                image = articles[0].select("img")[0]

# download image
img_data = requests.get(image["src"]).content
with open("image.jpeg", "wb") as file:
    file.write(img_data)

# email settings
env = dict(dotenv_values(".env"))
gmail_user = env["gmail_user"]
gmail_password = env["gmail_password"]

client_names = env["client_names"].split(",")
client_emails = env["client_emails"].split()

for i in range(len(client_names)):

    client_name = client_names[i]
    client_email = client_emails[i]

    message = f"Subject: Daily Article from Medium\n" \
              f"Hello again {client_name}! Take a look at the todays article.\n" \
              f"Author: {author}\n" \
              f"Title: {title}\n" \
              f"Description: {description}\n"

    # get current date dd/mm/YY H:M:S
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # send email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, client_email, message)
        server.close()
        print(f"Email sent to {client_name} at {current_date}.")
    except:
        print("Something went wrong...")

    i = i+1
