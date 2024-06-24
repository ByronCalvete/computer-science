# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average span confidence

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()

count = 0
total = 0

for line in fhand:
  line = line.rstrip()
  if line.startswith('X-DSPAM-Confidence:'):
    count = count + 1
    pos = line.find(':')
    value = line[pos + 1:].strip()
    numeric = float(value)
    total = total + numeric

print('Average spam confidence:', total/count)
