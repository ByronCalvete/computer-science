# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by finding the time string and then splitting that string into parts usig in the colon character. Once you have accumulated the counts for each hour, print our the counts, one per line, sorted by hour as shown below.

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print('Cannot be opened file', fname)
  exit()

hours = dict()

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From '): continue
  words = line.split()
  time = words[5]
  h,m,s = time.split(':')
  hours[h] = hours.get(h, 0) + 1

lst = [ (x,y) for x,y in hours.items() ]
lst.sort()

for (key,value) in lst:
  print(key, value)
