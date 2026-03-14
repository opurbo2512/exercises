#Currency Conversion

amount_from = int(input("How many euros are you exchanging? "))
rate_from = float(input("What is the exchange rate? "))

rate_to = 100
amount_to = (amount_from * rate_from) / rate_to

print(f"{amount_from} euros at an exchange rate of {rate_from} is")
print(f"{amount_to} U.S. dollars.")