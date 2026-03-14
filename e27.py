#Validating Inputs

def val(nam1,nam2,id,zip):
    is_any_wrong = False
    char_list = [chr(i) for i in range(97,122)] + [chr(i) for i in range(65,90)]
    num_list = [str(i) for i in range(10)]

    def name_char_wrong(nam):
        num = 0
        for i in nam:
            if i in char_list:
                num += 1
        if num == len(nam):
            return False
        return True
    
    if nam1 == "":
        print("The first name must be filled in.")
        is_any_wrong = True
    if len(nam1) <=2 or name_char_wrong(nam1):
        print(f"{nam1} is not a valid first name. It is too short.")
        is_any_wrong = True

    if len(nam2) <=2 or name_char_wrong(nam2):
        print("The last name must be filled in.")
        is_any_wrong = True

    def id_checker(id):
        if id[2] != "-":
            return "not a valid id"
        if id[0] not in char_list or id[1] not in char_list:
            return "not a valid id"
        for i in id[3:]:
            if i not in num_list:
                return "not a valid id"
        return "a valid id"
    def is_zip_correct(zip):
        for i in zip:
            if i not in num_list:
                return False
        return True
    if is_zip_correct(zip):
        pass
    else:
        print("The ZIP code must be numeric.")
        is_any_wrong = True
    if id_checker(id) == "not a valid id":
        is_any_wrong = True
    print(f"{id} is {id_checker(id)}")

    if not is_any_wrong:
        print("There were no errors found.")

first_name = input("Enter the first name: ")
second_name = input("Enter the last name: ")
zip = input("Enter the ZIP code: ")
id = input("Enter an employee ID: ")

val(first_name,second_name,id,zip)




    