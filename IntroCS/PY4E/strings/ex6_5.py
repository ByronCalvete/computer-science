# Slicing strings
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use "find" and string slicing to extract the portion of the string after the colon character and the use the "float" function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find(':')
portion = str[pos+1:].strip()
number = float(portion)

print(number) 
