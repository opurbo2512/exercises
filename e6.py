#Retirement Calculator

from datetime import date

current_year = date.today().year

current_age = int(input("What is your age? "))
retire_age = int(input("At what age would you like to retire? "))

retire_year = current_year + (retire_age-current_age)
remaining_year = retire_age-current_age

print(f"You have {remaining_year} years left untill you can retire.")
print(f"It's {current_year}, so you can retire in {retire_year}")
