# Sometimes when programmers get bored or want to have a bit of fun, the add a harmless Easter Egg to their program.
# Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo".
# The program should behave normally for all other files which exist and don't exist.

## Here is a sample execution of the program:

# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt

# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

fname =  input('Enter a file name: ')

if fname == 'na na boo boo':
  print("NA NA BOO BOO TO YOU - You have been punk'd")
  exit()

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened {fname}')
  exit()

count = 0

for line in fhand:
  line = line.rstrip()
  if line.startswith('Subject:'):
    count = count + 1

print(f'There were {count} subject line in {fname}')
