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
    req_str = "http://reiseauskunft.bahn.de/bin/bhftafel.exe/dn?&rt=1&input=Hamburg+Hbf&time=07:45&date=%s&productsFilter=1000000000&start=1&boardType=arr&REQTrain_name=1518" % (day)

    print "Fetching Verbindungsinformationen..."
    req = requests.get(req_str)
    soup = BeautifulSoup(req.text)

    rows = soup.find_all('tr', {'id':re.compile('journeyRow_.*')})

    for row in rows:
        train = row.find_all('a', text=re.compile(".*ICE.*"))[0].text
        info = row.find_all('td', {'class':'ris'})
        delay = 0

        if (not info):
            print "Too far in the future; no delay info available yet."
            delay = -1

        elif (train_name in train):
            delay_info = info[0].find_all('span', text=re.compile(".*ca\. \+*"))

            # if there is info about a delay, there is a delay (duh)
            if (delay_info):

                # for some reason there may be more than 1 in the list
                for i in delay_info:
                    time = re.search(".*ca\. \+(.*)", i.text).groups()[0]
                    if (time > delay):
                        delay = time

                print "train: ", train_name
                print "delay: ", delay

        else:
            # TODO handle this like a grown-up.
            delay = -2
            print "something went terribly wrong. :("

        return {"train": train_name, "delay": delay}

if __name__ == "__main__":
    today = datetime.date.today()
    train_name = "ICE 1518"
    next_tuesday = next_tuesday(today).strftime("%d.%m.%y")
    print("Getting delay info for %s on tuesday, %s ..." % (train_name, next_tuesday))
    info = get_delay_info(next_tuesday, train_name)
    print info
    print info["delay"]
