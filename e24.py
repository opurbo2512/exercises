#Anagram Checker

def is_anagram(str1 , str2):
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i in str2:
            pass
        else:
            return False
    return True

print("Enter two strings and I'll tell you if they")
print("are anagrams:")
str_1 = input("Enter the first string:")
str_2 = input("Enter the second string:")

if is_anagram(str_1,str_2):
    print(f"{str_1} and {str_2} are anagrams.")
else:
    print(f"{str_1} and {str_2} are not anagrams.")