# Figure out which line of the next program is still not properly guarded.
# See if you construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

## Original program

# fhand = open('test.txt')
# for line in fhand:
#   words = line.split()
#   print('Debug:', words)
#   if len(words) == 0 : continue
#   if words[0] != 'From' : continue
#   print(words[2])

## New program with stronger guardian pattern

fhand = open('test.txt')
for line in fhand:
  words = line.split()
  # print('Debug:', words)
  if len(words) < 3: continue # We need to check that the len() of list must have at least three values
  if words[0] != 'From': continue
  print(words[2])
