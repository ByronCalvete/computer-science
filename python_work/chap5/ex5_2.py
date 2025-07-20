print('First test\n')
string1 = 'my_college'
string2 = 'my_university'

print(string1 == string2) # False
print(string1 != string2) # True

print('\n---')

print('Second test\n')
tech_brand = 'Samsung'

print(tech_brand == 'samsung') # False
print(tech_brand.lower() == 'samsung') # True

print('\n---')

print('Third test\n')
pedro = 10
carlos = 14
juana = 12
andres = 12
camilo = 11

print(carlos > juana) # True
print(juana >= andres) # True
print(pedro < camilo) # True
print(pedro < camilo < andres) # True
print(pedro == juana) # False
print(andres != carlos) # True

print('\n---')

print('Fourth test\n')
carlos_height = 180
andrew_height = 183

print(carlos_height >= 180 and andrew_height < 190) # True
print(carlos_height > 190 or andrew_height > 180) # True

print('\n---')

print('Fifth test\n')
salad = ['lettuce', 'corn', 'onion', 'tomato', 'cheese']

print('cheese' in salad) # True
print('chicken' in salad) # False

print('\n---')

print('Sixth test\n')
basketball_team = ['lebron', 'kobe', 'curry', 'green', 'garnett']

print('lewis' not in basketball_team) # True
print('lebron' not in basketball_team) # False
