## Tuples and dictionaries
# d = dict()
# d['hello'] = 1
# d['world'] = 2

# for (k,v) in d.items():
#   print(k, v)

# print(d) # {'hello': 1, 'world': 2}
# tups = d.items()
# print(tups) # dict_items([('hello', 1), ('world', 2)])

## Sort by values instead of key
# d = { 'a': 10, 'c': 22, 'b': 1 }
# tmp = list()

# for (k,v) in d.items():
#   tmp.append((v, k))

# tmp = sorted(tmp, reverse=True)

# print(tmp)

## The top 10 most common words
# fhand = open('romeo.txt')

# counts = dict()

# for line in fhand:
#   line = line.rstrip()
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word, 0) + 1

# lst = list()

# for (k,v) in counts.items():
#   lst.append((v,k))

# lst = sorted(lst, reverse=True)

# for (v,k) in lst[:10]:
#   print(k,v)

## Even shorter version
fhand = open('romeo.txt')

counts = dict()

for line in fhand:
  line = line.rstrip()
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

lst = sorted([ (v,k) for (k,v) in counts.items() ], reverse=True)

for (v,k) in lst[:10]:
  print(k,v)
