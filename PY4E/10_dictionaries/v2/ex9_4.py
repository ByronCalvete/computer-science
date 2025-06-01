# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary as been created, look through the dictionary using a maximum loop to find who has the most messages and print how many messages the person has.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be openend: {fname}')
  exit()

emails = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  if len(words) < 2 or words[0] != 'From': continue
  
  mail = words[1]
  emails[mail] = emails.get(mail, 0) + 1

maxNum = max(emails.values())

for key in emails:
  if emails[key] == maxNum:
    print(key, emails[key])
