
from bs4 import BeautifulSoup
import requests
from urllib3 import *
import mechanize
url = 'http://useragentstring.com/'
response = requests.get(url)
visited_urls = set(url)
if response.status_code == 200:
    print('[+]: connection successful!')
    soup = BeautifulSoup(response.content, 'html parser')
    a_tag = soup.find_all('a')
    print(a_tag)
    url = []
    for tag in a_tag:
        href = tag.get("href")
         


else:
    print('[-]: connection could not be established')