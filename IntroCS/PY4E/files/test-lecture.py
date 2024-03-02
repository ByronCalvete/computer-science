fname = input('Enter the file name: ')

try:
  fhand = open(fname)
except:
  print('Fle cannot be opened:', fname)
  quit()

count = 0
for line in fhand:
  count = count + 1

print(f'The file {fname} has {count} lines')
