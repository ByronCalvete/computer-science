# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and de minimum of the numbers instead of the average. When enter 'done', too.
min_number = None
max_number = None

while True:
  num = input('Enter a number: ')

  if num == 'done':
    break
  
  try:
    num = int(num)
  except:
    print('Invalid input')
    continue

  if max_number is None or num > max_number:
    max_number = num

  if min_number is None or num < min_number:
    min_number = num


print('Maximum is', max_number)
print('Minimum is', min_number)