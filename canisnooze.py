#!/usr/bin/env python
import requests
import datetime
import re
from bs4 import BeautifulSoup

def next_tuesday(day):
    days_ahead = 1 - day.weekday()

    if days_ahead < 0:
        days_ahead += 7

    return day + datetime.timedelta(days_ahead)

def get_delay_info(day, train_name):
    #train_name = "ICE"
    day = "03.10.14"
    req_str = "http://reiseauskunft.bahn.de/bin/bhftafel.exe/dn?&rt=1&input=Berlin+Hbf&time=12:00&date=%s&productsFilter=1000000000&start=1&boardType=arr&REQTrain_name=209" % (day)

    print "Fetching Verbindungsinformationen..."
    req = requests.get(req_str)
    soup = BeautifulSoup(req.text)

    rows = soup.find_all('tr', {'id':re.compile('journeyRow_.*')})

    for row in rows:
        train = row.find_all('a', text=re.compile(".*ICE.*"))[0].text
        info = row.find_all('td', {'class':'ris'})[0]

        if (train_name in train):
            delay_info = info.find_all('span', text=re.compile(".*ca\. \+*"))
            delay = 0

            # if there is info about a delay, there is a delay (duh)
            if (delay_info):

                # for some reason there may be more than 1 in the list
                for i in delay_info:
                    time = re.search(".*ca\. \+(.*)", i.text).groups()[0]
                    if (time > delay):
                        delay = time

                print "train: ", train_name
                print "delay: ", delay

            return {"train", train_name, "delay", delay}

if __name__ == "__main__":
    today = datetime.date.today()
    train_name = "ICE  209"
    next_tuesday = next_tuesday(today).strftime("%d.%m.%y")
    print("Getting delay info for %s on tuesday, %s ..." % (train_name, next_tuesday))
    #print get_delay_info(next_tuesday, train_name)
    print get_delay_info(today.strftime("%d.%m.%y"), train_name)

