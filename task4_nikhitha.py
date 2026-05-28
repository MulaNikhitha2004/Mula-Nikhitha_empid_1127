temperature = float(input("Enter temperature in Celsius: "))

print("\n===== TEMPERATURE ADVICE =====")

if temperature < 0:
    print("Freezing! Stay indoors and wear heavy clothing")

elif temperature >= 0 and temperature <= 15:
    print("Cold. A jacket is recommended")

elif temperature >= 16 and temperature <= 25:
    print("Pleasant weather! Great for outdoor activities")

elif temperature >= 26 and temperature <= 35:
    print("Hot. Stay hydrated and use sunscreen")

else:
    print("Extreme heat! Avoid going outside")

print("================================")
