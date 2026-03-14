#Password Strength Indicator

def indicator(pawo):
    num_list = [str(i) for i in range(10)]
    small_letter = [chr(i) for i in range(97,122)]
    big_letter = [chr(i) for i in range(65,90)]
    letters = small_letter + big_letter

    length = len(pawo)
    num_letter = 0
    num_numb = 0

    for i in pawo:
        if i in num_list:
            num_numb += 1
        elif i in letters:
            num_letter += 1

    if length == num_numb and length < 8:
        return "a very weak password"
    if length == num_letter and length < 8:
        return "a weak password"
    if length >= 8 and (num_letter+ num_numb)==length:
        return "a strong password"
    if length >= 8 and (num_letter+ num_numb) < length:
        return "a very strong password"
    
pas = input("Enter the password: ")
pas_type = indicator(pas)

print(f"The passwrd '{pas}' is {pas_type}")



