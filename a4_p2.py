# 350111
# a4_p2.py
# Amish Kapri
# a.kapri@jacobs-universty.de

Name = input("Enter any string : ")
def count_Vowels(Name):
    num_Vowels=0
    for char in Name:
        if char in 'aeiouAEIOU':
            num_Vowels = num_Vowels+1
    return num_Vowels
while(Name):
    p = count_Vowels(Name)
    print("The number of Vowels letter in", Name, "is", p ,".")
    Name = input("Enter a string to continue or not to exist = ")
