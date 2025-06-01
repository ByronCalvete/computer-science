# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters 'done'.
# Write the program to store the numbers the user enters in alist and use the __max()__ and __min()__ functions to compute the maximum and minimum numbers after the loop completes.

numberList = list()

while True:
  inp = input('Enter a number: ')

  if inp == 'done':
    break

  try:
    number = float(inp)
  except:
    print(f'Error, please enter a numeric input')
    continue

  numberList.append(number)

print(f'Maximum: {max(numberList)}')
print(f'Minimum: {min(numberList)}')
