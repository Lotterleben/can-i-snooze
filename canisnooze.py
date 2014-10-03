#!/usr/bin/env python
import requests
import re
from bs4 import BeautifulSoup

# TODO: add correct day (-> aus woche ableiten?)
ICE_name = "ICE  209"
#ICE_name = "ICE"
req_str = "http://reiseauskunft.bahn.de/bin/bhftafel.exe/dn?&rt=1&input=Berlin+Hbf&time=12:00&date=03.10.14&productsFilter=1000000000&start=1&boardType=arr&REQTrain_name=209"

print "fetching Verbindungsinformationen..."
req = requests.get(req_str)
soup = BeautifulSoup(req.text)

rows = soup.find_all('tr', {'id':re.compile('journeyRow_.*')})

for row in rows:
    train = row.find_all('a', text=re.compile(".*ICE.*"))[0].text
    info = row.find_all('td', {'class':'ris'})[0]

    if (ICE_name in train):
        delay_info = info.find_all('span', text=re.compile(".*ca\. \+*"))
        delay = 0

        # if there is info about a delay, there is a delay (duh)
        if (delay_info):

            # for some reason there may be more than 1 in the list
            for i in delay_info:
                time = re.search(".*ca\. \+(.*)", i.text).groups()[0]
                if (time > delay):
                    delay = time

            print "train: ", ICE_name
            print "delay: ", delay

        # TODO: return instead of print
        print {"train", ICE_name, "delay", delay}











'''
req_str = "http://reiseauskunft.bahn.de/bin/query.exe/dn?revia=yes&existOptimizePrice=1&country=DEU&dbkanal_007=L01_S01_D001_KIN0001_qf-bahn_LZ003&ignoreTypeCheck=yes&S=BERLIN&REQ0JourneyStopsSID=&REQ0JourneyStopsS0A=7&Z=HAMBURG&REQ0JourneyStopsZID=&REQ0JourneyStopsZ0A=7&trip-type=single&date=Di%2C+07.10.14&time=05%3A45&timesel=depart&returnTimesel=depart&optimize=0&travelProfile=-1&adult-number=1&children-number=0&infant-number=0&tariffTravellerType.1=E&tariffTravellerReductionClass.1=0&tariffTravellerAge.1=&qf-trav-bday-1=&tariffTravellerReductionClass.2=0&tariffTravellerReductionClass.3=0&tariffTravellerReductionClass.4=0&tariffTravellerReductionClass.5=0&tariffClass=2&start=1&qf.bahn.button.suchen="

print "fetching Verbindungsinformationen..."
req = requests.get(req_str)
soup = BeautifulSoup(req.text)

times = soup.find_all('td', {'class':"time"})[1:-1]
print times, "\n xxxxxxxxxxxx"
print type(times)

time = soup.find('td', {'class':"time"}, text=re.compile(".*45.*"))
print time
'''