# Rewrite the grade program from the previous chapter using a function called __computergrade__ that takes a score as its parameter and returns a grade as a string

# Score     Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       F

try:
  score = float(input('Enter score: '))
except:
  print('Error, please entrar a numeric input')
  quit()

def computergrade(score):
  if score < 0 or score > 1:
    return 'Bad score'
  
  if score >= 0.9:
    return 'A'
  elif score >= 0.8:
    return 'B'
  elif score >= 0.7:
    return 'C'
  elif score >= 0.6:
    return 'D'
  else:
    return 'F'

x = computergrade(score)
print(x)
