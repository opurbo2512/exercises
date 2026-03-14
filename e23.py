#Troubleshooting Car Issues

print("Answer in this way. y for 'Yes' and n for 'n'")

q1 = input("s the car silent when you turn the key?")
if q1 == "y":
    q2 = input("Are the battery terminals corroded?")
    if q2 == "y":
        print("Clean terminals and try starting again.")
    else:
        print("Replace cables and try again.")

else:
    q3 = input("Does the car make a clicking noise?")
    if q3 == "y":
        print("Replace the battery.")
    else:
        q4 = input("Does the car crank up but fail to start?")
        if q4 == "y":
            print("Check spark plug connections.")
        else:
            q5 = input("Does the engine start and then die?")
            if q5 == "y":
                q6 = input("Does your car have fuel injection?")
                if q6 == "y":
                    print("Get it in for service.")
                else:
                    print("Check to ensure the choke is opening and closing.")