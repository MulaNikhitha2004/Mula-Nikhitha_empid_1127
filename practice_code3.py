# Temperature Converter

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp = float(input("Enter temperature in Celsius: "))

result = celsius_to_fahrenheit(temp)

print("Temperature in Fahrenheit:", result)
