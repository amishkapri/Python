list =[]
number = int(input("Enter the length of list :"))
print("Enter Number")
for i in range(0,number):
    data = int(input())
    c = list.append(data)

def smallest(lip):
    m = 99999999
    for i in range(0,len(lip)):
        if lip[i]<m:
            m=lip[i]
    return(m)

print("The smallest number in the list is",smallest(list),".")
