# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re

fhand = open('assigment-text.txt')

numbers = list()

for line in fhand:
  line = line.rstrip()
  x = re.findall('[0-9]+', line)
  if len(x) == 0: continue

  for number in x:
    numbers.append(int(number))
  
print(sum(numbers))

# Shortest version
print(sum([ int(x) for x in re.findall('[0-9]+', open('assigment-text.txt').read()) ]))
