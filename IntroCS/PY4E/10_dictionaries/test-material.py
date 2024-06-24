## Histogram with "if" statement
# word = 'brontosaurus'

# d = dict()

# for c in word:
#   if c not in d:
#     d[c] = 1
#   else:
#     d[c] = d[c] + 1

# print(d) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

## Histogram with "get" method
# word = 'brontosaurus'

# d = dict()

# for c in word:
#   d[c] = d.get(c, 0) + 1

# print(d) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

## Nested loop pattern for count words in a simple file romeo.txt
# fname =  input('Enter a file: ') # romeo.txt file

# try:
#   fhand = open(fname)
# except:
#   print('File cannot be opened:', fname)
#   exit()

# counts = dict()
# for line in fhand:
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word, 0) + 1

# print(counts) # {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

## Sort the key in alphabetical order
# friends = { 'chuck': 1, 'annie': 42, 'jan': 100 }

# lst = list(friends.keys())
# print(lst) # ['chuck', 'annie', 'jan']
# lst.sort()
# print(lst)
# for key in lst:
#   print(key, friends[key]) # Print the key-value pairs in alphabetical order

## Nested loop pattern for count words in a file romeo.txt with punctuation
import string

fname = input('Enter file name: ') # romeo-punc.txt file

try:
  fhand = open(fname)
except:
  print('File cannot be opened', fname)
  exit()

counts = dict()
for line in fhand:
  line = line.rstrip()
  # First two parameters are empty strings
  line = line.translate(line.maketrans('', '', string.punctuation))
  line = line.lower()
  words = line.split()

  for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts) # {'but': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'it': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'juliet': 1, 'sun': 2, 'arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}
