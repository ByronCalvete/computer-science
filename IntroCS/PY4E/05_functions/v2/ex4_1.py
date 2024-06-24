# Run the program on your system and see what numbers you get. Run the program more that once and see what numbers you get.
# The __random__ function is only one of many functions that handle random numbers. The function __randint__ takes parameters "low" and "high", and return an integer between "low" and "high" (including both).

import random

for i in range(10):
  x = random.random()
  print(x)

# First run
# 0.9638655597553879
# 0.032783880759261086
# 0.3970241156650526
# 0.2006995157240543
# 0.8825776656020038
# 0.2880606414709347
# 0.20418922136820028
# 0.0070627043582250915
# 0.16469678388234732
# 0.4677847993373183

# Second run
# 0.7848379768713986
# 0.7550115025388281
# 0.14295908107287114
# 0.19895135799544783
# 0.1143672848717957
# 0.7518451871593008
# 0.0074854411203112425
# 0.8902229723975535
# 0.9663457924831365
# 0.574960477898944

### randint function

y = random.randint(5, 10)
print(y) # Number between 5 and 10 (including both)

### choice function

t = [1,2,3]
z = random.choice(t)
print(z) # Choose an element from a sequence (t array in this case) at random
