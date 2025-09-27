#!bin/python3
import requests
import BeautifulSoup as bs4


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter the url you wish to use')
requests = request.get(url)
response = requests.response
port = input('Enter the port you wish to use for connection')
socket.connect(url, port)

if response.status_code == 200:
  while True:
    data = sock.recv(4096)
    print(data)
  if not data:
    break
  print(data.decode('utf8' errors='ignore')
  sock.close()

