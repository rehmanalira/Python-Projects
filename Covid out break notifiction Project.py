"""
Author: Rehman Ali RA
dated=25 auguest 2020

A Program which gives covid 19 notifiction
"""

from plyer import notification # module for notifiction
import requests
from bs4 import BeautifulSoup # beautify all the html data
import time
def notif_me(title,message): # notifiction function which igave notifiction in our pc

        notification.notify(
            title=title,
            message=message,
            app_icon='R:\Projects of Python\covid2.ico',
            timeout=6
        )

def getData(url):   # getting data from the web
    r=requests.get(url)
    return r.text
if __name__ == '__main__':

    #notif_me("Jutt sb","Rehman Ali RA")
    html_data=getData('http://covid.gov.pk/')
    #print(html_data) it will print all html data

    soup=BeautifulSoup(html_data,'html.parser') # it will beautify html data
   # print(soup.prettify())  # it will print the beautiful data

    dataStr= "" # here we stored all the sting means anchor tags
    for anchor in soup.find_all('a'): # here we find all the a means anchor tag
       """print(anchor) #it will print all anchor tag in data"""
       dataStr +=anchor.get_text() # here we adding the text form of anchor tags in string

    states=['Punjab','Islamabad','Balochistan'] # give the states name
    itemlist=dataStr.split("\n\n") # split to get all them in orders
    for item in itemlist[0:4]: # pick up first lines
        datList=item.split("\n")  # also split all the item
        if datList[1] in states: # here we get the postition which is in states
            nTitle='Covid-19 in Pakistan details by RA'
            nText=f"Cases in {datList[1]} are {datList[0]}"
            notif_me(nTitle,nText)
            time.sleep(5)


"""
If you want that it will run anf give notifiction after every hour and when you want 
usr while true and use time.sleep() mode
"""
