# Final innovative

from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
from tkinter import *


'''
html_text = requests.get("https://www.indiatoday.in/india").text

# print(type(html_text))
html_soup = BeautifulSoup(html_text, "lxml")
# print(type(html_soup))

#this will have all news
news = html_soup.find_all("div", class_ = "catagory-listing")

Newsdata=[]
Datadic={"Title":"", "Discription":""}


for i in news:    
    Datadic["Title"] = i.h2.a.text
    Datadic["Discription"] = i.p.text
    # headlines.append(i.h2.a.text)
    # shortnews.append(i.p.text)
    Newsdata.append(Datadic)
    # print(Datadic)
print(Newsdata)
    

'''

#################### Lets build and GUI NOW #########################

userdetails=[]


def login():
    global name
    global mailid
    global password
    global news_data
    name = enter_name.get()
    mailid = enter_Mail.get()
    userdetails.append({name:mailid})
    print(userdetails)
    if userdetails[0][name] == mailid:
        welcome_massage = Label(root,text=f"Welcome {name} to daily news")
        welcome_massage.grid(row=0, column=0)
        enter_name.grid_forget()
        enter_Mail.grid_forget()
        login_button.grid_forget()
        Namelabel.grid_forget()
        Maillabel.grid_forget()



root = Tk()

#name
root.title("News update")

Namelabel = Label(root, text="Enter your Name")
Namelabel.grid(row=0, column=0)
enter_name = Entry(root, width=25)
enter_name.grid(row=0,column=3)

Maillabel = Label(root, text="Enter your Mail-id")
Maillabel.grid(row=1, column=0)
enter_Mail = Entry(root, width=25)
enter_Mail.grid(row=1,column=3)

#button
login_button = Button(root, text="Login", command=login)
login_button.grid(row=3, column=1, pady=20)


root.mainloop()