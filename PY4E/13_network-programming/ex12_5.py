# (Advanced) Change the socket program so that it only shows data after the headers
# and a blank line have been received. Remenber that __recv__ receives characters (newlines and all), not lines

import socket

inputUrl = input('Enter url - ')

try:
  urlParts = inputUrl.split('/')
  hostname = urlParts[2]

  mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  mysock.connect((hostname, 80))
except:
  print('Invalid url', inputUrl)
  exit()

cmd = f'GET {inputUrl} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

counts = 0
bytesData = b''
byteMark = b'\r\n\r\n'
lst = list()

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  bytesData = bytesData + data
  decodeData = data.decode()
  counts += 1

  # Check existent url
  words = decodeData.split()
  if counts == 1 and words[1] != '200':
    print('Non-existent url', inputUrl)
    exit()

# Print contents without headers
posMark = bytesData.find(byteMark)
contents = bytesData[posMark + len(byteMark):].decode()

# Count the number of characters
words = contents.split()
for word in words:
  lst.append(len(word))

print(contents)
print(f'The total characters are {sum(lst)}')

mysock.close()
