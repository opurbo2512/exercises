#Blood Alcohol Calculator

alcohol = float(input("Enter total alcohol consumed, in ounces (oz) "))
w = float(input("Enter body weight in pounds "))
sex = input("men or women : ")
sex = sex.lower()
if sex == "men" or sex == "women":
    pass
else:
    print("Please enter men or women")
    sex = input("men or women : ")
    sex = sex.lower()
hour = int(input("Enter number of hours since the last drink "))

if sex == "men":
    ratio = 0.73
else:
    ratio = 0.66
BAC = ((alcohol*5.14) / (w*ratio)) - (0.015 * hour)

if BAC >= 0.08:
    print("It is not legal for you to drive.")
else:
    print("It is legal for you to drive.")