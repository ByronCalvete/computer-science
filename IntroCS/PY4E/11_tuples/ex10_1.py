# Revise a previous program as follow: Read and parse the "From" lines and pull out the addresses fromt he line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)

except:
  print('File cannot be opened', fname)
  quit()

addresses = dict()

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  mail = words[1]
  addresses[mail] = addresses.get(mail, 0) + 1

lst = list()

for (key, value) in addresses.items():
  lst.append((value, key))

lst.sort(reverse=True)

count, mail = lst[0]

print(mail, count)
