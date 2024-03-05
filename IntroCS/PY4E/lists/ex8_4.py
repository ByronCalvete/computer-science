# Find all unique words in a file

fhand = open('romeo.txt')

unique_words = list()

for line in fhand:
  words = line.split()

  for word in words:
    if word in unique_words:
      continue
    unique_words.append(word)

  unique_words.sort()

print(unique_words)
