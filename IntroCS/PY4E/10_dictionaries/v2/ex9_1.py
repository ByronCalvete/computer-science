# Write a program that reads the words.txt and stores them as keys in a dictionary. It doesn't matter what the values are.
# Then you can use the __in__ operator as a fast way to check whether a string is in the dictionary.

fhand = open('words.txt')

allWords = dict()

for line in fhand:
  words = line.split()
  if len(words) == 0: continue
  for word in words:
    if word in allWords:
      continue
    allWords[word] = 1
  
print(allWords)
print('behalf' in allWords) # True
print('hardware' in allWords) # True
print('software' in allWords) # False
