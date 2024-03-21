# ## Using "re.search()" like "find()"
# # find()
# hand = open('mbox-short.txt')
# for line in hand:
#   line = line.rstrip()
#   if line.find('From:') >= 0:
#     print(line)

# # re.search()
# import re

# fhand = open('mbox-short.txt')
# for line in fhand:
#   line = line.rstrip()
#   if re.search('From:', line):
#     print(line)

# <---------->

# ## Using "re.search()" like "startswith()"
# # startswith()
# hand = open('mbox-short.txt')
# for line in hand:
#   line = line.rstrip()
#   if line.startswith('From:'):
#     print(line)

# # re.search()
# import re

# fhand = open('mbox-short.txt')
# for line in fhand:
#   line = line.rstrip()
#   if re.search('^From:', line):
#     print(line)

# <---------->

# ## Fine-Tuning your match
# import re

# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   if re.search('^X-\S+:', line):
#     print(line)

# <---------->
import re

## Matching and Extracting Data
x = 'My 2 favorite number are 19 and 42'
y = re.findall('[0-9]+', x)
print(y) # ['2', '19', '42']
y = re.findall('[AEIOU]+', x)
print(y) # []

## Warning: Greedy Matching
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y) # ['From: Using the :']

## Non-Greedy Matching
y = re.findall('^F.+?:', x)
print(y) # ['From:']

# <---------->

## Fine-Tuning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y) # ['stephen.marquard@uct.ac.za']
y = re.findall('^From \S+@\S+', x)
print(y) # ['From stephen.marquard@uct.ac.za']
y = re.findall('^From (\S+@\S+)', x)
print(y) # ['From stephen.marquard@uct.ac.za']

# <---------->

## Extracting the domain
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', x)
print(y) # ['uct.ac.za']

# <---------->

## Spam confidence average
import re
fhand = open('mbox-short.txt')

lst = list()
for line in fhand:
  line = line.rstrip()
  stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
  if len(stuff) != 1: continue
  numFloat = float(stuff[0])
  lst.append(numFloat)

print('Maximum:', max(lst)) # Maximum: 0.9907

# <---------->

## Escape Character
import re

x = 'We just receive $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(y) # ['$10.00']
