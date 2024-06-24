# Write a program to prompt for a score between 0.0 and 1.0. If the scaore is out of range, print an error message. If the score is betweeen 0.0 and 1.0, print a grae using the following table:

# Score     Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       F

try:
  score = float(input('Enter score: '))
except:
  print('Bad score')
  quit()

if score < 0 or score > 1.0:
  print('Bad score')
  quit()

if score >= 0.9:
  print('A')
elif score >= 0.8:
  print('B')
elif score >= 0.7:
  print('C')
elif score >= 0.6:
  print('D')
else:
  print('F')
