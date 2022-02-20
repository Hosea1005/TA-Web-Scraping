from os import link
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.pegipegi.com/promo/?f=slider'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

items = soup.findAll('div','col-sm-6 col-md-4')

for peg in items : 
    name = peg.find('div','caption').find('p').text
    try : durasi = peg.find('p','endpromo')
    except : durasi = 'Tidak memiliki durasi'
    linknya = peg.find('a')['href']
    img = peg.find('div','thumbnail').find('img')['src']
    if 'http' not in img : img = 'https://www.pegipegi.com/promo/{}'.format(img)
    print(img)