# Rewrite your pay computation with time-and-a-half for overtime and create a function called __computepay__ which takes two parameters (__hours__ and __rate__).

try:
  hours = float(input('Enter Hours: '))
  rate = float(input('Enter Rate: '))
except:
  print('Error, please enter numeric input')
  quit()

def computepay(fh, fr):
  if fh > 40:
    regPay = fh * fr
    overtime = (fh - 40)*(fr * 0.5)
    total = regPay + overtime
  else:
    total = fh * fr
  
  return total

pay = computepay(hours, rate)

print(f'Pay: ${pay}')
