# Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression and the __findall()__ method.
# Compute the average of the numbers and print out the average as an integer.

import re

fname = input('Enter file: ')

try:
  fhand= open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

numbers = list()

for line in fhand:
  line =  line.rstrip()
  x = re.findall('^New Revision: ([0-9]+)', line)
  if len(x) == 0: continue
  
  x = int(x[0])
  numbers.append(x)

average = sum(numbers)//len(numbers)

print(average)
