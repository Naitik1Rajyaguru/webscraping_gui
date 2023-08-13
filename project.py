from tabulate import tabulate
import smtplib
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from cProfile import label
from tkinter import *

import certifi
ca = certifi.where()

cluster = MongoClient(
    "mongodb+srv://the-deltaw:uqzb8HVXDKxVHxm@decagon.gymkl.mongodb.net/newsScrapper?retryWrites=true&w=majority", tlsCAFile=ca)

db = cluster["newsScrapper"]
collection_newsScrapper = db["newsScrapper"]
collection_mailingList = db["mailing"]


def fetchDataAndStore():
    html_text = requests.get("https://www.indiatoday.in/india").text
    html_soup = BeautifulSoup(html_text, "lxml")
    news = html_soup.find_all("div", class_="B1S3_content__thumbnail__wrap__iPgcS content__thumbnail__wrap")
    data = []

    for i in news:
        data.append({
            "title": i.h2.a.text,
            "description": i.p.text
        })
    print(data)
    collection_newsScrapper.insert_many(data)


def takeMail():
    os.system(
        "py Final_innovative.py")

def sendMail():

    mails = collection_mailingList.find({})
    mail_to_send = set()
    for document in mails:
        print(document)
        mail_to_send.add(document['email'])
    print(mail_to_send)


    your_gmail = 'riskyrick20@gmail.com'
    app_password = 'rwunrvohokqgrsyg'
    subject = f'NewsScrapper Email {datetime.datetime.now()}'

    body = '<font color="coral"><h1>Welcome to your daily short newsletter</h1></font>'
    
    news = collection_newsScrapper.find({})
    # fresh_news = set()
    # for i in news:
    #     fresh_news.add(i)

    for i in news:
        s = f"<font color='#0c8599'><h2>{i['title']}</h2></font><p>{i['description']}</p>"
        body = " ".join((body, s))
    print(body)

    

    try:
        msg = MIMEMultipart()
        msg['From'] = your_gmail
        msg['To'] = ", ".join(mail_to_send)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(your_gmail, app_password)
        text = msg.as_string()
        server.sendmail(your_gmail, mail_to_send, text)
        server.quit()

        print("Emails sent successfully !")

    except Exception as e:
        print(e)


while True:
    opts = [
        ["1", "Fetch the news from the website"],
        ["2", "Insert your email into the system"],
        ["3", "Send the mail to all participents (For admin only)"]
    ]
    head = ["Choice", "Description"]
    print(tabulate(opts, headers=head, tablefmt="grid"))
    choice = int(input())
    if choice == 1:
        fetchDataAndStore()
    elif choice == 2:
        takeMail()
    elif choice == 3:
        sendMail()
    else:
        break
