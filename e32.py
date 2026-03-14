#Guess the Number Game

import random

print("Let's play Guess the Number.")
level = int(input("Pick a difficulty level (1, 2, or 3): "))
if level == 1:
    end = 10
    print("Guess between 1 to 10")
    target = random.randint(1,10)
elif level == 2:
    end = 100
    print("Guess between 1 to 100")
    target = random.randint(1,100)
else:
    end = 1000
    print("Guess between 1 to 1000")
    target = random.randint(1,1000)

a = 0
while True:
    if a==0:
        num = int(input("I have my number. What's your guess? "))
    a += 1
    if num < target:
        num = int(input("Too low. Guess again: "))
    elif num > target:
        num = int(input("Too high. Guess again: "))
    else:
        print(f"You got it in {a} guesses!")
        again = input("Play again? y/n: ")
        if again == "y":
            a = 0
        else:
            print("Goodbye!")
            break

