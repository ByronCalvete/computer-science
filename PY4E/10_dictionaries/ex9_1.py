# Write a program that reads the words in 'words.txt' and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the "in" operator as a fast way to check whether a string is in the dictionary.

fhand = open('words.txt')

myDictionary = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()

  for word in words:
    myDictionary[word] = 1

# print(myDictionary) # Prints all the items (key-value pairs) created from words.txt file.
print('mind-numbing' in myDictionary) # True
print('computer' in myDictionary) # True
print('another' in myDictionary) # False
