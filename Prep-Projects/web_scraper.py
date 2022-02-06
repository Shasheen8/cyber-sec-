#implementing a web scraper

from ipaddress import summarize_address_range
from bs4 import BeautifulSoup
import csv
import requests

source = requests.get('https://healthybyte.net').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open ('','')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print (headline)

    summary = article.find('div',class='youtube-player')['src']