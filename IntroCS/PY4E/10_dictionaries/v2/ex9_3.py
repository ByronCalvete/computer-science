# Write a program that read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

mails = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  if len(words) < 2 or words[0] != 'From': continue
  mail = words[1]

  mails[mail] = mails.get(mail, 0) + 1

print(mails)
