#Handling Bad Input

import math
while True:
    try:
        prompt = input("What is the rate of return? ")
        rate = float(prompt)
        if rate == 0:
            print("Sorry. That's not a valid input.")
        else:
            year = math.ceil(72/rate)
            print(f"It will take {year} years to double your initial investment.")
            break
    except:
        print("Sorry. That's not a valid input.")
    
