#Temperature Converter: Fahrenheit to Celcius

print("\n Hey there, welcome to the FC Temperature Calculator \n")

print('Please enter your temperature in Farenheit: \n')
temperature = input()


fahrenheit = int(temperature) - 32

celcius = int(fahrenheit) / 1.8


print('Your temperature is ', str(round(celcius,2)) , ' degree celcius')
