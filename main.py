import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values, load_dotenv
from datetime import datetime
import smtplib
import schedule
import time
import os

load_dotenv('.env')

env = dict(dotenv_values(".env"))
gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_PASSWORD")

client_names = os.getenv("CLIENT_NAMES").split(",")
client_emails = os.getenv("CLIENT_EMAILS").split()
client_tags = os.getenv("CLIENT_TAGS").split()

def job():
    # loop for send special email everyone in list "client_emails"
    for i in range(len(client_names)):
        print("Program started successfully!")

        # get page source code with requests
        client_tag = client_tags[i]
        url = f"https://medium.com/tag/{client_tag}"
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

        # get last article's link
        link = articles[0].select("a")[3]["href"]
        if "http" in link:
            pass
        else:
            link = f"https://medium.com{link}"

        # try to get last article's image
        # try:
        #     image = articles[0].select("img")[4]
        # except IndexError:
        #     try:
        #         image = articles[0].select("img")[3]
        #     except IndexError:
        #         try:
        #             image = articles[0].select("img")[2]
        #         except IndexError:
        #             try:
        #                 image = articles[0].select("img")[1]
        #             except IndexError:
        #                 image = articles[0].select("img")[0]

        # download image
        # img_data = requests.get(image["src"]).content
        # with open("image.jpeg", "wb") as file:
        #     file.write(img_data)

        client_name = client_names[i]
        client_email = client_emails[i]

        message = f"Subject: Daily Article from Medium\n" \
                  f"Hello again {client_name}! Take a look at the todays article.\n" \
                  f"Tag: {client_tag}\n" \
                  f"Author: {author}\n" \
                  f"Title: {title}\n" \
                  f"Description: {description}\n" \
                  f"Read full article here: {link}"

        message = message.encode("utf-8")

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
        except Exception as e:
            print(e)
        i = i+1
    else:
        print("Program finished successfully!")

# Run script every day at 12.00
# schedule.every().day.at("20:00").do(job)
# schedule.every(1).minutes.do(job) # every minute for now in test time
#
# while 1:
#     schedule.run_pending()
#     time.sleep(1)

job()
