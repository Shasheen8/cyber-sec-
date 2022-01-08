#implementing a web scraper

from bs4 import BeautifulSoup
import csv
import requests

source = requests.get('https://healthybyte.net').text

soup = BeautifulSoup(source, 'lxml')
