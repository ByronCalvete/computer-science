## Minimalist Email Client

# MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which stores emails consecutively.
# Emails are separated by a special line which starts with From (notice the space). Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator.
# Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

# Write a program to read through the mail box and data when you find line that starts with "From", you will split the line into words using the __split__ function.
# We are interested in who sent the message, which is the second word on the From line.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.

fname =  input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

count = 0

for line in fhand:
  words = line.split()
  if len(words) < 2 or words[0] != 'From': continue
  count = count + 1
  print(words[1])

print(f'There were {count} lines in the file with From as the first word')
