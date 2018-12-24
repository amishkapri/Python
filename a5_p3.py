# 350111
# a5_p3.py
# Amish Kapri
# a.kapri@jacobs-universty.de

check = True
arr = []
i=0
while check:
    temp = input("Enter Value:")
    if temp != 0:
        arr.append(temp)
        i += 1
    else:
        check = False
print("Maximum value:" + str(max(arr)))
print("Minimum values:" + str(min(arr)))
#This program is not working and I coudn't fix it. 
