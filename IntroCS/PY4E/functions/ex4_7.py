# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as string.

# Score     Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       F

try:
  scoreinput = float(input('Enter score: '))
except:
  print('Bad score')
  quit()

def computegrade(score):
  if(score < 0.0 or score >= 10.0 ):
    return 'Bad score'
  elif(score >= 0.9):
    return 'A'
  elif(score >= 0.8):
    return 'B'
  elif(score >= 0.7):
    return 'C'
  elif(score >= 0.6):
    return 'D'
  else:
    return 'F'

x = computegrade(scoreinput)
print(x)
  