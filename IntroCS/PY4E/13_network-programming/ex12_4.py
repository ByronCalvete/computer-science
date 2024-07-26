# Change the __urllinks.py__ program to extract and count paragraph (p) tags from the retrieved HTML document
# and display the count of the paragraphs as the output of your program.
# Do not display the paragraph text, only count them.
# Test your program on several small web pages as well as some larger web pages

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inputUrl = input('Enter url - ')

try:
  htmlPage = urllib.request.urlopen(inputUrl, context=ctx).read()
except:
  print('Invalid url', inputUrl)
  exit()

soup = BeautifulSoup(htmlPage, 'html.parser')
tags = soup('a')

print(f'There are {len(tags)} paragraph (a) tags in {inputUrl} HTML document')
