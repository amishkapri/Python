# 350111
# a3_p5.py
# Amish Kapri
# a.kapri@jacobs-universty.de


C = float(input("Enter the volume of Water in cups = "))
D = float(input("Enter the volume of Water in gallons = "))
def to_litre(D,C) :
    d_l = D*3.7854
    c_l = C*0.2366
    return(d_l + c_l)
P = to_litre(D,C)
print("the volume after conversion is ", P ,"litres .")
