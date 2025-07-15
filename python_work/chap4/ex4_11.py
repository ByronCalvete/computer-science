pizzas = ['fugazzata', 'muzzarella', 'napolitana']
friend_pizzas = pizzas[:]

pizzas.append('hawaiana')
friend_pizzas.append('ranch')

print('My favorite pizzas are:')
for pizza in pizzas:
  print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza.title())
