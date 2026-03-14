#Computing Statistics

def max_v(l):
    ans = l[0]
    for i in l:
        if i > ans:
            ans = i
    return ans

def min_v(l):
    ans = l[0]
    for i in l:
        if i < ans:
            ans = i
    return ans

def average(l):
    sum = 0
    length = len(l)
    for i in l:
        sum += i
    return sum / length

def sd(l):
    mean = average(l)
    square_diff_list = []
    for i in l:
        square_diff = (mean - i)**2
        square_diff_list.append(square_diff)
    square_diff_mean = average(square_diff_list)
    return square_diff_mean ** 0.5

l = []
while True:
    prompt = input("Enter a number: ")
    if prompt == "done":
        break
    l.append(int(prompt))

print("Numbers: ",end="")
length = len(l)
for i in range(length):
    if i == length-1:
        print(l[i])
    else:
        print(l[i],end=", ")

print(f"The average is {average(l)}")
print(f"The maximum is {max_v(l)}")
print(f"The minimum is {min_v(l)}")
print(f"The standard deviation is {sd(l)}")
