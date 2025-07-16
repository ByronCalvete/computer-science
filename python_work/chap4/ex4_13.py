foods = ('pizza', 'hamburguer', 'chicken', 'fish', 'meatballs')
# foods[1] = 'spaguetti' # This line produces an error, TypeError
print('The menu:')
for food in foods:
  print(food.title())

print('\nUpdated menu:')
foods_updated = ('pizza', 'hamburguer', 'chicken', 'spaguetti', 'tacos')
for food in foods_updated:
  print(food.title())
