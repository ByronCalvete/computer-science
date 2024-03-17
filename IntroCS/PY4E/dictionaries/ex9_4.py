# Add code to previous program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop to find who has the most messages and print how many messages the person has.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print('File cannot be opened', fname)
  exit()

emailAddress = dict()
bigCount = None
bigEmail = None

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  email = words[1]
  emailAddress[email] = emailAddress.get(email, 0) + 1

for key,value in emailAddress.items():
  if bigCount is None or value > bigCount:
    bigCount = value
    bigEmail = key

print(bigEmail, bigCount)
