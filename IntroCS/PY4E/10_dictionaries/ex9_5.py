# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print('File cannot be opened', fname)
  exit()

domains = dict()

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  emailAddres = words[1]
  dn = emailAddres.split('@')[1]
  domains[dn] = domains.get(dn, 0) + 1

print(domains)
