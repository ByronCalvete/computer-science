basketball = ['rebounds', 'points', 'triples', 'assists', 'steals', 'blocks', 'turnovers']
print('Initial list:')
print(basketball)

del basketball[0]
basketball.insert(0, 'rebounds')
basketball.pop()
basketball.append('turnovers')
basketball.append('other')
basketball.remove('other')
sorted(basketball)
basketball.reverse()
basketball.reverse()

print('Final list:')
print(basketball)
