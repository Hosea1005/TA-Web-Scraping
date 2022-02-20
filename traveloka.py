from os import link
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.traveloka.com/en-id/promotion'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
req = requests.get(url, headers=headers)
# print(req)

soup = BeautifulSoup(req.text,'html.parser')
items = soup.findAll('div','promo-thumb')
for tra in items:
    # name = tra.find('div','promo-thumb-desc').text
    # duration = tra.find('div','promo-thumb-duration').text
    # linknya = tra.find('a')['href']
    image = tra.find('div','promo-thumb-img').find('img')['src']
    print(image)