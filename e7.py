#Area of a Rectangular Room

length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))

area_feet = length * width
area_meter = area_feet*0.09290304

print(f"You entered dimensions of {length} feet by {width} feet.")
print("The area is")
print(f"{area_feet} square feet")
print(f"{area_meter} square meters")