#Multistate Sales Tax Calculator

amount = float(input("What is the order amount?"))
state = input("What state do you live in? ")
state = state.lower()

if state == "wisconsin":
    country = input("What country do you live in? ")
    country = country.lower()
    if country == "clair":
        tax = 0.05 * amount
    else:
        tax = 0.04 * amount

else:
    tax = 0.08 * amount

total = amount + tax
print(f"The tax is ${tax}.")
print(f"The total is ${total}.")