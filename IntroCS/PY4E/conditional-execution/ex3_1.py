# Rewrite you pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

fh = float(hours)
fr = float(rate)

if fh > 40.0:
  regPay = fh * fr
  overtime = (fh - 40)*(fr * 0.5)
  pay = regPay + overtime
else:
  pay = fh * fr

print('Pay:', pay)