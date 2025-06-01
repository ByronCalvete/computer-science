## Find all unique words in a file

# Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand?
# Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file __romeo.txt__ containing a subset of Shakespeare’s work.
# Create a list of unique words, which will contain the final result. Write a program to open the file __romeo.txt__ and read it line by line.
# For each line, split the line into a list of words using the __split__ function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

fhand = open('romeo.txt')

uniqueWords = list()

for line in fhand:
  words = line.split()

  for word in words:
    if word in uniqueWords:
      continue
    uniqueWords.append(word)

uniqueWords.sort()

print(uniqueWords)
