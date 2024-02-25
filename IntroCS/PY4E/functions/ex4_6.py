# Rewrite you pay computation with time-and-a-half for overtimeand create a function called computepay which take two parameters (hours and rate)

try:
  hrs = float(input('Enter Hours: '))
  rt = float(input('Enter Rate: '))
except:
  print('Error, please enter numeric input')
  quit()

def computerpay(hours, rate):
  if(hours > 40.0):
    regpay = hours * rate
    overtime = (hours - 40)*(rate * 0.5)
    pay = regpay + overtime
  else:
    pay = hours * rate
  
  return pay

pay = computerpay(hrs, rt)

print('Pay:', pay)
