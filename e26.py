#Months to Pay Off a Credit Card

import math

def calculation(rate,payment,balance):
    i = rate/365
    upper = math.log10(1+(balance/payment)*(1-((1+i)**30)))
    lower = math.log10(1+i)
    if lower == 0:
        return "Error: Monthly payment is too low to cover interest."
    n_month = (-1/30) * (upper/lower)
    return math.ceil(n_month)

bal = float(input("What is your balance? "))
per = float(input("What is the APR on the card (as a percent)? "))
pay = float(input("What is the monthly payment you can make? "))

n_month = calculation(per/100,pay,bal)
print(f"It will take you {n_month} months to pay off this card.")