# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, prionting each letter on a separate line, except backwards

str = 'basketball'
index = len(str) - 1

while index >= 0:
  print(str[index], index)
  index = index - 1
