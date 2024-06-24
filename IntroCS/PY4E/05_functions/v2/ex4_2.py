# Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

## Original program

# def print_lyrics():
#   print("I'm a lumberjack, and I'm okay.")
#   print('I sleep all night and I work all day.')

# def repeat_lyrics():
#   print_lyrics()
#   print_lyrics()

# repeat_lyrics()

## Move the last line to the top

repeat_lyrics() # Error, because Python didn't find the function and definition. The message is "repeat_lyrics" is not defined

def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

def repeat_lyrics():
  print_lyrics()
  print_lyrics()
