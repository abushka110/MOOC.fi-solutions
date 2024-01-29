fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32.0) * (5.0/9.0)
if celsius < 0:
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius" + "\nBrr! It's cold in here!")
else:
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")