#Numbers to Names

num = int(input("Please enter the number of the month:"))
idx = num - 1

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
month = months[idx]

print(f"The name of the month is {month}.")