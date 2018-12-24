# 350111
# a5_p2.py
# Amish Kapri
# a.kapri@jacobs-universty.de

def histogram(lst):
    for i in lst:
        print("*"*int(i))

list1 = []
number= int(input("Enter list length "))
print("Enter number")
while len(list1) !=number:
    data = (input())
    list1.append(data)
histogram(list1)
