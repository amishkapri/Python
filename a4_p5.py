# 350111
# a4_p5.py
# Amish Kapri
# a.kapri@jacobs-universty.de

readfile = open("numbers.txt", 'r')
readfileinput = readfile.readlines()
p=0
for line in readfileinput:
    try:
        k = int(line)
        p = p + k
    except ValueError:
        print("Invalid Input")

print("The sum of all numbers in the file is", p ,".")
