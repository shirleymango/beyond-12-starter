import requests
from bs4 import BeautifulSoup
import csv

# Cal State
URL = "https://www.csueastbay.edu/registrar/important-dates/fall-2021.html"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

events=[]
table = soup.find('table') 
rows = table.find_all('tr')

for row in rows:
    event = {}
    if row.find('td', attrs = {'width':'410'}) == None:
        continue
    if row.find('td', attrs = {'width':'410'}).text == '':
        continue
    event['college'] = "Cal State"
    event['name'] = row.find('td', attrs = {'width':'410'}).text
    event['date'] = row.find('td', attrs = {'width':'245'}).text
    events.append(event)

# UC Davis
URL = 'https://registrar.ucdavis.edu/calendar/web/master'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify)

table = soup.find('div', attrs = {'aria-label':'Scrollable Table'})
rows = table.find_all('tr')
# print(table)

# San Francisco State
URL = "https://registrar.sfsu.edu/deadlines"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify)

table = soup.find('table') 
rows = table.find_all('tr')
events2 = []

for row in rows:
    cells = row.find_all('td')
    event = ["San Francisco State"]
    for cell in cells:
        event.append(cell.text)
    events2.append(event)
print(events2)
