#Picking a Winner

import random
l = []
while True:
    prompt = input("Enter a name: ")
    if prompt == "":
        break
    l.append(prompt)

winner = random.choice(l)
print(f"The winner is {winner}")
