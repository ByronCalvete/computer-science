# Revise a previous progras as follows: Read and parse de 'From' lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

counts = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  if len(words) < 2 or words[0] != 'From': continue
  email = words[1]

  counts[email] = counts.get(email, 0) + 1

lst = list()

for key,val in counts.items():
  lst.append((val, key))

lst.sort(reverse=True)

count, mail = lst[0]

print(mail, count)
