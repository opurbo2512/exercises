#Computing Simple Interest

principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate of interest: "))
year = float(input("Enter the number of years: "))

invesment_worth = principal + principal * (rate / 100) * year

print(f"After {year} years at {rate}%, the investment will")
print(f"be worth ${invesment_worth}.")