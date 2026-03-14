#Paint Calculator

length = int(input("Enter length of the ceiling: "))
width = int(input("Enter width of the ceiling: "))

area = length*width
gallon = area / 350

if gallon == int(gallon):
    gallon = int(gallon)
else:
    gallon += 1
    gallon = int(gallon)

print(f"You will need to purchase {gallon} gallons of paint to cover {area} square feet.")