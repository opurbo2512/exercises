#Filtering Values

def even(l):
    even_list = []
    for i in l:
        if i%2 == 0:
            even_list.append(i)
    return even_list

prompt = input("Enter a list of numbers, separated by spaces: ")
l1 = prompt.split()
l2 = [int(i) for i in l1]
l3 = even(l2)

print("The even numbers are ",end="")
length = len(l3)
for i in range(length):
    if i == length-1:
        print(l3[i],end=".")
    else:
        print(l3[i],end=" ")