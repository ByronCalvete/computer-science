# Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket

LIMIT_CHARACTERS = 3000
BUFFER_ITERATIONS = 10
BUFFER = int(LIMIT_CHARACTERS/BUFFER_ITERATIONS)

inputUrl = input('Enter url - ')

try:
  urlParts = inputUrl.split('/')
  hostname = urlParts[2]
  mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  mysock.connect((hostname, 80))
except:
  print(f'Invalid url {inputUrl}')
  exit()

cmd = f'GET {inputUrl} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

counts = 0
lst = list()

while True:
  data = mysock.recv(BUFFER)
  if len(data) < 1:
    break
  decodeData = data.decode()
  words = decodeData.split()
  
  # Check existent URL
  counts += 1
  if counts == 1 and words[1] != '200':
    print('Non-existent URL', inputUrl)
    exit()

  if counts <= BUFFER_ITERATIONS:
    print(decodeData, end='\n')

  for word in words:
    lst.append(len(word))

print(f'The total characters are {sum(lst)}')

mysock.close()
