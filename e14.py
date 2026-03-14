#Tax Calculator

amount = float(input("What is the order amount? "))
state = input("What is the state? ")

if state == "WI":
    subtotal = amount
    tax_rate = 5.5
    tax = subtotal * (tax_rate/100)
    total = subtotal + tax
    print(f"The subtotal is ${subtotal}.")
    print(f"The tax is ${tax}.")
    print(f"The total is ${total}.")

else:
    total = amount
    print(f"The total is ${total}.")