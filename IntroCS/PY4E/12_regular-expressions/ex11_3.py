# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re

fhand = open('assigment-text.txt')

lst = list()

for line in fhand:
  line = line.rstrip()
  numbers = re.findall('[0-9]+', line)
  if len(numbers) == 0: continue
  for num in numbers:
    intNum = int(num)
    lst.append(intNum)

print(sum(lst))

## Shortest version
print(sum([ int(x) for x in re.findall('[0-9]+', open('assigment-text.txt').read()) ]))