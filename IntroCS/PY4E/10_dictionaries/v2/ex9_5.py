# This program records the domain name (instead of the addres) where the message was sent from instead of who mail came from (i.e., the whole mail address).
# At the end of the program, print out the contents of your dictionary.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

domainNames = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  if len(words) < 2 or words[0] != 'From': continue

  emailAddress = words[1]
  dn = emailAddress.split('@')[1]

  # Histogram
  domainNames[dn] = domainNames.get(dn, 0) + 1

print(domainNames)
