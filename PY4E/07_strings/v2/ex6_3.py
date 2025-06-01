# Encapsulate the next code in a funtion name __count__, and generalize it so that it accepts the string and the letter as arguments.

## Code to encapsulate

# word = 'banana'
# count = 0

# for letter in word:
#   if letter == 'a':
#     count = count + 1

# print(count)

def count(str, letter):
  count = 0

  for x in str:
    if x == letter:
      count = count + 1
  
  return f"The letter '{letter}' appears {count} times in {str} word"

x = count('banana', 'a')

print(x)
