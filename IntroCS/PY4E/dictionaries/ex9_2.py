# Write a program that categorizes each email message by which day of the week the commit was done. To do this look for that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (orders does not matter).

# Sample line "From stephen.marquard@uct.ac.za San Jan 5 09:14:16 2008"

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print('File cannot be opened', fname)
  exit()

daysOfTheWeek = dict()

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  day = words[2]
  # Histogram
  daysOfTheWeek[day] = daysOfTheWeek.get(day, 0) + 1

print(daysOfTheWeek)
