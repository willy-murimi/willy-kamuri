import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set() #filtering out duplicate urls by deleting them
def spider_urls(url, keyword):
    try:
        response = request.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        print(urls)

        
            
        for urls2 in urls:
            if urls2 not in visited_urls():
                visited_urls.add(urls2)# this enables link clicking by opening them up
                url_join = urljoin(url, urls2) #this translate url to absolute url from relative url i.e it will follow the rule https://www.THISisEXAMPLE.com
    #checking for keyword
                if keyword in url_join:
                        print(url_join)
                        spider_urls(url_join, keyword)
            else:
                pass



    url = input("Enter the url you want to scrap. ")
    keyword = input("enter the keyword you want to search for in the url provided. ")
    spider_urls(url, keyword)