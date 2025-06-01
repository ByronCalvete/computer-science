# Slicing strings
# Take the following Python code that stores a string:
# __str = 'X-DSPAM-Confidence: 0.8475'__
# Use __find__ and string slicing to extract the portion of the string after the colon character and then use the __float__ function to convert the extracted string into a floating point number

str = 'X-DSPAM-Confidence: 0.8475'
colonPos = str.find(':')
portion = str[colonPos + 1:]
number = float(portion)

print(number)
