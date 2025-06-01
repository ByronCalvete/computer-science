# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines start with 'From', then look for the third word and keep a running count each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).

## Sample line

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

## Sample execution:

# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

days = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  if len(words) < 3 or words[0] != 'From': continue
  day = words[2]
  # Histogram
  days[day] = days.get(day, 0) + 1

print(days)
