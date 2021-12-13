<h1 align="center">Daily Article from <a href="https://medium.com/">Medium</a></h1>

## ✏️ About 
* A web scraping project that automatically sends you a Medium article on a topic to your email address daily. (at 12.00 GMT+00.00)
* Uses Heroku servers.

## 🐍 Librarys I used
|Library|Version|Usage|
|-------|-------|------|
|requests|2.26.0|Get page source code|
|beautifulsoup4|4.10.0|Parse page source code|
|python-dotenv|0.19.1|Get sensitive data from .env file|
|smtplib|-|Send mail|
|schedule|1.1.0|Run script every day at 12.00|

## 🧐 How to Use
* First install project.
````bash
$ git clone https://github.com/orhanemree/Daily-Article-from-Medium.git
$ cd Daily-Article-from-Medium
$ pip3 install -r requirements.txt
````
* Create .env file and fill it yourself.
* Be careful about commas and spaces.
````
GMAIL_USER = "<sender_user_mail>"
GMAIL_PASSWORD = "<sender_user_password>"
CLIENT_NAMES = "<receiver_name_1>,<receiver_name_2>"
CLIENT_EMAILS = "<receiver_mail_1> <receiver_mail_2>"
CLIENT_TAGS = "<receiver_1_tag> <receiver_2_tag>"
````
* Run.
````bash
$ python main.py
````

* Lastly, deploy code to Heroku.

### or
* Just answer [this](https://forms.gle/MXgsoKW4aFfLEWD8A) Google Form and I'll add your name to our receiver list.

## ☑️ To Do
* [ ] Added article images to emails

## 📃 License
* This project is licensed under the [MIT
License](https://github.com/orhanemree/Daily-Article-from-Medium/blob/master/LICENSE)

