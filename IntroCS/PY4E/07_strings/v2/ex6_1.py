# Write a __while__ loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

word = 'obstacle'
index = len(word) - 1

while index >= 0:
  letter = word[index]
  print(letter)
  index = index - 1

## Another way

# word = 'obstacle'
# index = 1

# while index <= len(word):
#   letter = word[-index]
#   print(letter)
#   index = index + 1
