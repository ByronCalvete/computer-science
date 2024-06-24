# Write a simple program to simulate the operation of the "grep" command on Unix. Aske the user to enter a regular expression and count the number of lines that matched the regular expression
import re

file = open('mbox.txt')
userRegEx = input('Enter a regular expression: ')

count = 0

for line in file:
  line = line.rstrip()
  x = re.findall(userRegEx, line)
  if len(x) > 0:
    count += 1

print(f'mbox.txt had {count} lines that matched {userRegEx}')
