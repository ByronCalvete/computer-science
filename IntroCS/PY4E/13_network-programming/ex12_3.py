# Use __urllib__ to replicate the previous exercise (1) retrieving the document from a URL, (2) displaying up to 3000 characters,
# and (3) counting the overall number of characters in the document. Don't worry about the headers for this exercise,
# simply show the first 3000 characters of the document contents.

import urllib.request

LIMIT_CHARACTERS = 3000

inputUrl = input('Enter url - ')

try:
  fhand = urllib.request.urlopen(inputUrl)
except:
  print('Invalid URL', inputUrl)
  exit()

lst = list()

for line in fhand:
  line = line.decode().strip()

  if sum(lst) <= LIMIT_CHARACTERS:
    print(line)

  words = line.split()

  for word in words:
    lst.append(len(word))

print(f'\nThe total characters are {sum(lst)}')
