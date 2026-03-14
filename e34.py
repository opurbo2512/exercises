#Employee List Removal

l = [
    "John Smith",
    "Jackie Jackson",
    "Chris Jones",
    "Amanda Cullen",
    "Jeremy Goodwin",
]

print(f"There are {len(l)} employee:")
for i in l:
    print(i)
print()

employee = input("Enter an employee name to remove: ")
l.remove(employee)

print(f"There are {len(l)} employee:")
for i in l:
    print(i)