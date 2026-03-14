#Counting the Number of Characters

prompt = input("What is the input string ? ")

character_num = len(prompt)

if prompt == "":
    print("Enter something first!")

else:
    print(f"{prompt} has {character_num} characters.")