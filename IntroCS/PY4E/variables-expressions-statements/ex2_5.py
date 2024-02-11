# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

promptCelsius = input('Please enter your current temperature in Celsius degrees:\n')
tempC = float(promptCelsius)
tempF = (tempC * (9/5) + 32)

print('The temperature in Fahrenheit degrees is', tempF)
