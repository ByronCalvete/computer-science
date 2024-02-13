# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of the range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# Score     Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       F

score = input('Enter score: ')

try:
  scr = float(score)
except:
  print('Bad score')
  quit()

if scr < 0.0 or scr > 1.0:
  print('Bad score')
  quit()

if scr >= 0.9:
  print('A')
elif scr >= 0.8:
  print('B')
elif scr >= 0.7:
  print('C')
elif scr >= 0.6:
  print('D')
else:
  print('F')
