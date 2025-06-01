## Sort a list of words from longest to shortest
# txt = 'but soft what light in yonder window breaks'
# words = txt.split()

# t = list()
# for word in words:
#   t.append((len(word), word))

# t.sort(reverse=True)

# res = list()

# for len, word in t:
#   res.append(word)

# print(res)

## Dictionaries and tuples
# d = { 'b': 1, 'a': 20, 'c': 22 }
# t = list(d.items())
# print(t) # [('b', 1), ('a', 20), ('c', 22)]
# t.sort()
# print(t) # [('a', 20), ('b', 1), ('c', 22)]

## Multiple assigment with dictionaries
# d = { 'a': 10, 'b': 1, 'c': 22 }
# l = list()

# for key, val in d.items():
#   l.append( (val, key) )

# l.sort(reverse=True)

# print(l) # [(22, 'c'), (10, 'a'), (1, 'b')]

## The most common word
# import string
# fhand = open('romeo-punc.txt')

# counts = dict()
# for line in fhand:
#   line = line.rstrip()
#   line = line.translate(str.maketrans('', '', string.punctuation))
#   line = line.lower()
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word, 0) + 1

# # Sort de dictionary by value
# lst = list()
# for key,value in counts.items():
#   lst.append( (value, key) )

# lst.sort(reverse=True)

# for value, key in lst[:10]:
#   print(key, value)

## Usign tuples as keys in dictionaries
# first = 'byron'
# last = 'calvete'
# number = 12214252

# d = dict()
# d[last, first] = number

# for last, first in d:
#   print(first, last, d[last, first]) # byron calvete 12214252

# print(d) # {('calvete', 'byron'): 12214252}

## List comprehension
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = []

for x in list_of_ints_in_strings:
  list_of_ints.append(int(x))

print(sum(list_of_ints)) # 119
# With list comprehension, the above code can be written in a mnore compact manner
list_of_ints_in_strings2 = ['42', '65', '12']
list_of_ints2 = [ int(x) for x in list_of_ints_in_strings2 ]
print(sum(list_of_ints2)) # 119
