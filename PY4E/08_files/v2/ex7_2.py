# Write a program to prompt for a file name, and then read through the file and look for line of the form:

# X-DSPAM-Confidence: 0.8475

# When you encounter a line that start with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print put the average spam confidence.

## Execution examples

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened: {fname}')
  exit()

total = 0
count = 0

for line in fhand:
  line = line.rstrip()
  if not line.startswith('X-DSPAM-Confidence:'): continue
  
  numberPos = line.find(':')
  portion = line[numberPos + 1:].strip()
  number = float(portion)

  total = total + number
  count = count + 1

print(f'Average spam confidence: {round((total / count), 12)}')
