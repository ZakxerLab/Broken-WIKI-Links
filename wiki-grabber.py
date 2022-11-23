import requests
from bs4 import BeautifulSoup
import csv
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
links = []
with open('linki-wiki.csv', newline='') as f:
    for row in csv.reader(f):
        links.append(row[0])

externals_list = []

for link in links:
    response = requests.get(link, headers=headers, allow_redirects=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    externals = soup.find_all('a', class_='external text')
    for external in externals:
        match = re.search('wikimedia.*|web.archive.*|wikipedia.*|creativecommons.*|worldcat.org/.*', str(external)
                          , flags=re.I)
        if match:
            pass
        else:
            file_object = open('link.txt', 'a+')
            file_object.write(external['href'] + '\n')
            file_object.close()
            externals_list.append(external['href'])
