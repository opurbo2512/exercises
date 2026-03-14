#Self-Checkout

price_1 = int(input("Enter the price of item 1: "))
quantity_1 = int(input("Enter the quantity of item 1: "))
price_2 = int(input("Enter the price of item 2: "))
quantity_2 = int(input("Enter the quantity of item 2: "))
price_3 = int(input("Enter the price of item 3: "))
quantity_3 = int(input("Enter the quantity of item 3: "))

subtotal = price_1 * quantity_1 + price_2 * quantity_2 + price_3 * quantity_3
tax_rate = 5.5
tax = subtotal * (tax_rate / 100) 
total = subtotal + tax

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")