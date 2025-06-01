# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the lette a-z. Your program should not count spaces, digits, punctuation, or anything other than the letter a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.

import string

fname = input('Enter a file name: ')

try:
  fhand = open(fname)
except:
  print(f'File cannot be opened {fname}')
  exit()

letters = dict()

for line in fhand:
  line = line.rstrip()

  # Remove spaces, digits, punctuation
  line = line.translate(str.maketrans('','', string.whitespace))
  line = line.translate(str.maketrans('','', string.digits))
  line = line.translate(str.maketrans('','', string.punctuation))

  words = line.lower()

  for letter in words:
    letters[letter] = letters.get(letter, 0) + 1

lst = [ (val, key) for key,val in letters.items() ]
lst.sort(reverse=True)

allLetters = sum(letters.values())


for val,key in lst:
  percentage = round((val*100) / allLetters, 2)
  print(f'{key}: {percentage}%')


## Text en español

# e: 13.32%
# a: 11.23%
# s: 9.92%
# o: 9.14%
# u: 6.01%
# n: 6.01%
# r: 5.48%
# d: 5.22%
# i: 4.96%
# l: 4.7%
# c: 3.92%
# t: 3.66%
# p: 3.66%
# m: 3.13%
# q: 1.83%
# á: 1.31%
# h: 1.31%
# v: 1.04%
# y: 0.78%
# b: 0.78%
# z: 0.52%
# k: 0.52%
# g: 0.52%
# ú: 0.26%
# í: 0.26%
# é: 0.26%
# f: 0.26%

## English text

# e: 13.47%
# t: 10.03%
# i: 8.31%
# h: 7.45%
# a: 7.16%
# s: 6.88%
# n: 6.59%
# o: 5.73%
# r: 4.87%
# w: 4.3%
# l: 4.01%
# d: 3.44%
# y: 2.58%
# f: 2.58%
# m: 2.29%
# g: 2.29%
# v: 1.43%
# u: 1.43%
# k: 1.43%
# b: 1.43%
# p: 1.15%
# c: 0.86%
# j: 0.29%

