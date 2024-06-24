# Move the function call back to the bottom and move the definition of __print_lyrics__ after the definition of __repeat_lyrics__. What happens when you run this program?

## Original program

# def print_lyrics():
#   print("I'm a lumberjack, and I'm okay.")
#   print('I sleep all night and I work all day.')

# def repeat_lyrics():
#   print_lyrics()
#   print_lyrics()

# repeat_lyrics()

## Move the function call back to the bottom and....

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

repeat_lyrics() ## The program runs with no errors
