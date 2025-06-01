## Character matching in regular expressions

# # Search for line that start with 'F', followed by 2 characters, followed by 'm:'
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   if re.search('^F..m', line):
#     print(line)

# # Search for lines that start with From and have an at sign
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   if re.search('^From:.+@', line):
#     print(line)

## Extracting data using regular expression
    
# # Search for lines that have an at sign between characters
# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print(lst) # ['csev@umich.edu', 'cwen@iupui.edu']

# # Search for lines that have an at sign between characters
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   s = re.findall('\S+@\S+', line)
#   if len(s) > 0:
#     print(s)

# # Search for lines that have an at sign between characters and the characters must be a letter o number
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   s = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#   if len(s) > 0:
#     print(s)

## Combining searching and extracting

# # Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number. The number can include a decimal.
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   if re.search('^X\S*: [0-9.]+', line):
#     print(line)

# # Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number. The number can include a decimal. Then print the number id it is greater than zero.
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   s = re.findall('^X\S*: ([0-9.]+)', line)
#   if len(s) > 0:
#     print(s)

# # Search for lines that start with 'Details: rev=' followed by numbers, then print the number if one is found
# import re
# fhand = open('mbox-short.txt')

# for line in fhand:
#   line = line.rstrip()
#   s = re.findall('^Details:.*rev=([0-9]+)', line)
#   if len(s) > 0:
#     print(s)

# Search for lines that start with "From" and a character followed by a two digit number between 00 and 99 followed by ':'. Then print the number if one is found
import re
fhand = open('mbox-short.txt')

for line in fhand:
  line = line.rstrip()
  s = re.findall('^From .* ([0-9][0-9]):', line)
  if len(s) > 0:
    print(s)

# We can find money amounts
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)