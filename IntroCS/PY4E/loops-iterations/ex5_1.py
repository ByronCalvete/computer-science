# Write a program which repeatedly reads integers until the user enters 'done'. Once 'done' is entered, print out the total, count and average of the integers. If the user enters anything other that integers, detect their mistake using try and except and print an error message and skip to the next integers.

total = 0
count = 0

while True:
  num = input('Enter a integer number: ')

  if num == 'done':
    break
  
  try:
    num = int(num)
  except:
    print('Invalid input')
    continue

  total = total + num
  count = count + 1


print(total, count, round(total/count, 3))
