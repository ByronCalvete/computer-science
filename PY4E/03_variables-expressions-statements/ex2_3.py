# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) * float(rate)

print('Pay:', round(pay, 2)) # Limit to two decimal digits
