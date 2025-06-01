## With sockets

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#   data = mysock.recv(512)
#   if (len(data) < 1):
#     break
#   print(data.decode())

# mysock.close()

## With urllib

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#   words = line.decode().split() # Decode because this lines is bytes not string
#   for word in words:
#     counts[word] = counts.get(word, 0) + 1

# lst = list()

# for key,val in counts.items():
#   lst.append((val,key))

# lst.sort(reverse=True)

# for (value, key) in lst:
#   print(key,value)

## Reading Web Pages

# import urllib.request, urllib.parse, urllib.error, re

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#   print(line.decode().strip())

## Web Scraping

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
  print(tag.get('href', None))
