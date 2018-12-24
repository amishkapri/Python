# 350111
# a5_p1.py
# Amish Kapri
# a.kapri@jacobs-universty.de


list1 = []
number= int(input("Enter list length "))
print("Enter number")
while len(list1) !=number:
    data = float(input())
    list1.append(data)
    print(list1)
Value = 1.5
def add(list1,Value):
    for i in range(0,number):
        list1[i] = list1[i]+1.5
    return list1    
def multiply(list1,Value):
    for i in range(0,number):
        list1[i] = list1[i]*5
    return list1

print(add(list1,Value))
print(multiply(list1,Value))
