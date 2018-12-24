# 350111
# a4_p6.py
# Amish Kapri
# a.kapri@jacobs-universty.de

data = input("Enter the text file :")
readfile = open( data , "r")
readinputfile = readfile.readlines()
num = 0
for line in readinputfile:
    words = line.count(" ")
    num += 1
    print(" The total words in line", num ,"is", words+1 ,)
