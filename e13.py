#Determining Compound Interest

principal = float(input("What is the principal amount? "))
rate = float(input("What is the rate? "))
year = float(input("What is the number of years? "))
n_compund = float(input("What is the number of times the interest is compounded per year? "))

end_invesment = principal * (1 + (rate/100)/n_compund)**(n_compund*year)

print(f"${principal} invested at {rate}% for {year} years")
print(f"compounded {n_compund} times per year is ${end_invesment}.")
