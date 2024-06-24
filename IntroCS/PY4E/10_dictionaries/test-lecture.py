# counts = dict()

# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# for name in names:
#   counts[name] = counts.get(name, 0) + 1

# print(counts)

#### Counts the frequency of the words in a line of text

# counts = dict()

# line = input('Enter a line of text:') # the clown ran after the car and the car ran into the tend and the tend fell down on the clown and the car
# words = line.split()

# print('Words:', words)
# print('Counting...')

# for word in words:
#   counts[word] = counts.get(word, 0) + 1

# print('Counts', counts)

#### Counts words in a text file

name = input('Enter file: ')

try:
  fhand = open(name)
except:
  print('File cannot be openend', name)
  exit()

counts = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None

for word,count in counts.items():
  if bigCount is None or count > bigCount:
    bigWord = word
    bigCount = count

print(bigWord, bigCount)
