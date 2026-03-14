#Karvonen Heart Rate

def h_rate(rp,age,i):
    h_rate = ((220-age)-rp)*i + rp
    return int(h_rate)

pulse = int(input("Resting Pulse: "))
age = int(input("Age: "))

print("Intensity    | Rate")
print("-------------|-----")

for i in range(55,96,5):
    rate = h_rate(pulse,age,i/100)
    print(f"{i}%          | {rate} bpm")