# Encapsulate this code in a function named "count" and generalize it so that it accepts the string and the letter as arguments

def count(word, letter):
  count = 0
  for i in word:
    if i == letter:
      count = count + 1
  
  convert = str(count)
  print(f'the letter {letter} appears {convert} times on word {word}')

count('banana', 'a') # The letter a appears 3 times on word banana
