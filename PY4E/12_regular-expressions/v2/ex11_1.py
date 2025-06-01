# Write a simple program to simulate the operation of the __grep__ command on Unix. Ask the user to enter a regular expressio and count the number of lines that matched the regular expression:

import re

expression = input('Enter a regular expression: ')

if expression == '':
  print('Enter a valid regEx')
  quit()

fhand = open('mbox.txt')

count = 0

for line in fhand:
  line = line.rstrip()
  if not re.search(expression, line): continue
  count = count + 1

print(f'mbox.txt had {count} lines that matched {expression}')
