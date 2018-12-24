# 350111
# a2_p3.py
# Amish Kapri
# a.kapri@jacobs-universty.de

from sys import argv
script , input = argv
txt = open(input, 'r')
print("Here's your file :")
p = txt.read()
print(p)
p = str(ord(p[0])*ord(p[1]))

target = open("output", 'w')
target.write(p)
