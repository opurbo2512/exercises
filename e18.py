# Temperature Converter

print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
choice = input("Your choice: ")

if choice == "C":
    F = float(input("Please enter the temperature in Fahrenheit: "))
    C = (F - 32) * 5 / 9
    print(f"The temperature in Celsius is {C}.")

else:
    C = float(input("Please enter the temperature in Celsius: "))
    F = (C * 9 / 5) + 32
    print(f"The temperature in Farenheit is {F}.")
