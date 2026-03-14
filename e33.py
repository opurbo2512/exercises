#Magic 8 Ball

import random
ques = input("What's your question? ")
answers = ["Yes","No","Maybe","Ask again later"]
answer = random.choice(answers)

print(answer)
