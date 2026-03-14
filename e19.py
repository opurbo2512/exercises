#BMI Calculator
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter: "))

bmi = weight / (height**2)

if bmi >= 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}.")
    print(f"You are within the ideal weight range.")

elif bmi > 25:
    print(f"Your BMI is {bmi}.")
    print(f"You are overweight. You should see your doctor.")

else:
    print(f"Your BMI is {bmi}.")
    print(f"You are underweight. You should see your doctor.")