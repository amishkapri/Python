# 350111
# a5_p4.py
# Amish Kapri
# a.kapri@jacobs-universty.de

list1 = []
number= int(input("Enter list1 length "))
print("Enter number")
while len(list1) != number:
    data = input()
    list1.append(data)
    print(list1)
list2 = []
number= int(input("Enter list2 length "))
print("Enter number")
while len(list2) !=number:
    data = input()
    list2.append(data)
    print(list2)
ln = []
def overlapping(list1,list2):
    for i in list1:
        for  j  in list2:
            if i == j:
                return True;
    return False;

if overlapping(list1,list2) == True:
    print("The two lists are overlapping.")
else:
    print("The two lists are not overlapping")
