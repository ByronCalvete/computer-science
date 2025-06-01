# Write a function calles __chop__ that takes a list and modifies it, removing the first and last elements, and return __None__.
# The write a function calles __middle__ that takes a list and returns a new list that contains all but the first and last elements.

# Chop function

numbers = [1,2,3,4,5,6,7]

def chop(t):
  del t[0]
  del t[-1]

chop(numbers)
print(numbers) # [2,3,4,5,6]

# middle function

letters = ['r', 'o', 'c', 'k', 'y']

def middle(t):
  newt = t[1:-1]
  return newt

newLetters = middle(letters)

print(newLetters) # ['o', 'c', 'k']
print(letters) # ['r', 'o', 'c', 'k', 'y']
