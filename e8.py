#Pizza Pary

n_people = int(input("How many people? "))
n_pizza = int(input("How many pizza do you have?"))

n_pizza_piece = n_pizza * 8
one_get = (n_pizza_piece) // n_people
remain_piece = n_pizza_piece - (one_get * n_people)

print(f"{n_people} people with {n_pizza} pizzas")
print(f"Each person gets {one_get} pieces of pizza.")
print(f"There are {remain_piece} leftover pieces.")