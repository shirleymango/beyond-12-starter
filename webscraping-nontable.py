import requests
from bs4 import BeautifulSoup

URL = "https://laney.edu/instruction/departments-and-programs/academic-calendar/"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

events = soup.find_all("p")
array = []

for event in events:
    if "–" in event.text:
        data = event.text.split("–")
        array.append(data)

print(array)
