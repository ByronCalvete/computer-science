# Rewrite your pay program usign "try" and "except" so that your program handles non-numeric input gracefully by printing a messaage and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
  fh = float(input('Enter Hours: '))
  fr = float(input('Enter rate: '))
except:
  print('Error, please enter numeric input')
  quit()

if fh > 40:
  regPay = fh * fr
  overtime = (fh - 40)*(fr * 0.5)
  pay = regPay + overtime
else:
  pay = fh * fr

print(f'Pay: ${pay}')
