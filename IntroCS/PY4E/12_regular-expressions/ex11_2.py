# Write a program that look for lines of the form:
# "New Revision: 39772"
import re

fname = input('Enter a file: ')
try:
  fhand = open(fname)
except:
  print('File cannot be opened', fname)
  exit()

numbers = list()

for line in fhand:
  line = line.rstrip()
  s = re.findall('^New Revision: ([0-9]+)', line)
  if len(s) > 0:
    num = int(s[0])
    numbers.append(num)

print((sum(numbers)//len(numbers)))
