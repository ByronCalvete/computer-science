# Write a program which prompts the user for a Celcius temperature, convert the temperature to Fahrenheit, and print out the converted temperature

promptCelcius = input('Enter the Celsius temperature: ')
tempC = float(promptCelcius)
tempF = ((tempC)*(9/5)) + 32

print(f'{promptCelcius}°C is {tempF}°F')
