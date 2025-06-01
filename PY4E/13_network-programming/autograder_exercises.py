## One

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#   data = mysock.recv(512)
#   if len(data) < 1:
#     break
#   print(data.decode(), end='')

# mysock.close()

## Two

# import urllib.request
# import ssl
# from bs4 import BeautifulSoup

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# inputUrl = input('Enter url - ')
# html = urllib.request.urlopen(inputUrl, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# lst = list()
# count = 0

# spanTags = soup('span')
# for tag in spanTags:
#   content = tag.contents[0]
#   lst.append(int(content))
#   count += 1

# print(f'Count {count}')
# print(f'Sum {sum(lst)}')

## Three

import urllib.request
import ssl
import re
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


while count >= 0:
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser') 
  tags = soup('a')
  print(f'Retrieving: {url}')
  if count > 0:
    url = tags[position - 1].get('href')
  count -= 1

# Find the name of the ultimate valid url
ans = re.findall('^http.*_by_([^ ]*).html', url)

print(f'The answer to the assigment for this execution is "{ans[0]}".')