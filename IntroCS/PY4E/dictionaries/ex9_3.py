# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print('File cannot be opened', fname)
  exit()

emailAddress = dict()

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  mail = words[1]
  emailAddress[mail] = emailAddress.get(mail, 0) + 1

print(emailAddress)
