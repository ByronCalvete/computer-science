# Rewrite the guardian code in the next example without two __if__ statements.
# Instead, use a compound logical expression usign the __or__ logical operator with a single __if__ statement.

## Original program

# fhand = open('test.txt')
# for line in fhand:
#   words = line.split()
#   print('Debug:', words)
#   if len(words) == 0 : continue
#   if words[0] != 'From' : continue
#   print(words[2])

## New program

fhand = open('mbox-short.txt')

for line in fhand:
  words = line.split()
  if len(words) < 3 or words[0] != 'From': continue
  print(words[2])