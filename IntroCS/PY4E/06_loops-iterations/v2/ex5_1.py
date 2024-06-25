# Write a program which repeatedly reads integers until the user enter "done". Once "done" is entered, print out the total, count, and average of the integers. If the user enter anything other that integers, detect their mistake using __try__ and __except__ and print an error message and skip to the next integers.

count = 0
total = 0

while True:
  inputData = input('Enter a number: ')

  if inputData == 'done':
    break

  try:
    fdata = int(inputData)
  except:
    print('Invalid input')
    continue

  count = count + 1
  total = total + fdata
  average = total / count
  
  
print(f'{total} {count} {round(average, 3)}')
