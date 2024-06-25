# Write another program that prompts for a list of numbers as abover and at the end prints out both the maximum and minimum of the numbers instedad of the average.

maxNumber = None
minNumber = None

while True:
  inputData = input('Enter a number: ')

  if inputData == 'done':
    break

  try:
    fdata = int(inputData)
  except:
    print('Invalid input')
    continue
  
  if maxNumber is None or fdata > maxNumber:
    maxNumber = fdata
  
  if minNumber is None or fdata < minNumber:
    minNumber = fdata
  
print(f'The maximun is {maxNumber} and the minimum is {minNumber}')
