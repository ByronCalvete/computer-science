## The simplest web browser

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))

# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#   data = mysock.recv(512)
#   if len(data) < 1:
#     break
#   print(data.decode(), end='')

# mysock.close()

## Retrieving an image over HTTP

# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

# count = 0
# picture = b''

# while True:
#   data = mysock.recv(5120)
#   if len(data) < 1: break
#   time.sleep(0.25)
#   count = count + len(data)
#   print(len(data), count)
#   picture = picture + data

# mysock.close()

# # Look for the end of the header ( 2 CRLF)
# pos = picture.find(b'\r\n\r\n')
# print('Header Length', pos)
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open('stuff.jpg', 'wb')
# fhand.write(picture)
# fhand.close()

## Retrieving web pages with urllib

# import urllib.request

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# count = dict()

# for line in fhand:
#   line = line.decode().strip()
#   words = line.split()
#   if len(words) < 1: continue
#   for word in words:
#     count[word] = count.get(word, 0) + 1
  
# lst = list()

# for key,val in count.items():
#   lst.append((val, key))

# lst.sort(reverse=True)

# # for (value, key) in lst:
# #   print(key, value)

# [ print(key,value) for value,key in lst ]

## Reading binary files using urllib

# Read all data at once
import urllib.request, urllib.parse, urllib.error

img  = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('hola.jpg', 'wb')
fhand.write(img)
fhand.close()

# Read data in blocks (or buffers)
img2 = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand2 = open('hola2.jpg', 'wb')

size = 0
count = 0

while True:
  info = img2.read(100000)
  if len(info) < 1: break
  size = size + len(info)
  fhand2.write(info)
  count += 1

print(f'{size} characters copied in {count} buffers.')
fhand2.close()
