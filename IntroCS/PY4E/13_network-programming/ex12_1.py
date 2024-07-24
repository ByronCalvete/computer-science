# Change the socket program __socket1.py__ to prompt the user for the URL si it can read any web page.
# You can use __split('/')__ to break the URL into its component parts so you can extract the host name for the socket __conect__ call.
# Add error checking usign __try__ and __except__ to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket

inputUrl = input('Enter url - ')
urlParts = inputUrl.split('/')
hostname = urlParts[2]

try:
  mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  mysock.connect((hostname, 80))
except:
  print('Invalid URL', inputUrl)
  exit()

cmd = f'GET {inputUrl} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  print(data.decode(), end='')

mysock.close()
