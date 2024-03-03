numList = list()

while True:
  inp = input('Enter a number: ')
  if inp == 'done': break
  value = float(inp)
  numList.append(value)

average = sum(numList) / len(numList)
print('Average', average)

# Second program

# Print only the day of the week
fhand = open('mbox-short.txt')

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  print(words[2])

