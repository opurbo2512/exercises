#Password Generator

import random

num_list = [str(i) for i in range(1,10)]
letter_list = [chr(i) for i in range(97,122)] + [chr(i) for i in range(65,90)]
sp_char_list = ["!","@","#","$","%","&","_","-","^","*"]

min_len = int(input("What's the minimum length? "))
sp_ch = int(input("How many special characters? "))
num = int(input("How many numbers? "))

length = random.randint(min_len,min_len+3)
pas = []
char_num = length - (sp_ch + num)

for i in range(sp_ch):
    ch = random.choice(sp_char_list)
    pas.append(ch)
for i in range(num):
    ch = random.choice(num_list)
    pas.append(ch)
for i in range(char_num):
    ch = random.choice(letter_list)
    pas.append(ch)

final_pass = ""
while len(pas) != 0:
    ch = random.choice(pas)
    final_pass += ch
    pas.remove(ch)

print("Your password is")
print(final_pass)
