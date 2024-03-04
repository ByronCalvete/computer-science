# Write a function calles "chop" that takes a list and modifies it, removing the first and last elements, and returns None. The write a function calles "middle" that takes a list and returns a new list that contains all but the first and last elements.

# chop function
numbers = [0, 1, 2, 3, 4, 5]

def chop(t):
  del t[0]
  del t[len(t) - 1]

chop(numbers)
print(numbers) # [1, 2, 3, 4]

# middle function
letters = ['b', 'y', 'r', 'o', 'n']

def middle(t):
  return t[1:len(t) - 1]

newLetters = middle(letters)
print(newLetters) # ['y', 'r', 'o']
