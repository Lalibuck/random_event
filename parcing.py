import requests
from bs4 import BeautifulSoup

url = 'https://afisha.relax.by/theatre/minsk/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='schedule__event')
for item in items:
    itemName = item.find('a', class_='schedule__event-link link')
    itemHref = itemName['href']
    itemName = itemName.text.strip()
    itemDesc = item.find('a', class_='schedule__event-dscr text-black-light')
    if itemDesc is not None:
        itemDesc = itemDesc.text.strip()
    print(itemName, itemDesc, itemHref)