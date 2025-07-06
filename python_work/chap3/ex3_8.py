cities = ['tokio', 'istanbul', 'cairo', 'helsinki', 'dubai']
print('Original list:')
print(cities)

print('\nList sorted:')
print(sorted(cities))

print('\nOriginal list:')
print(cities)

print('\nList sorted reversed:')
print(sorted(cities, reverse=True))

print('\nOriginal list:')
print(cities)

print('\nList reversed:')
cities.reverse()
print(cities)

print('\nOriginal list:')
cities.reverse()
print(cities)

print('\nAlphabetical ordered list:')
cities.sort()
print(cities)

print('\nInverse alphabetical ordered list:')
cities.sort(reverse=True)
print(cities)
