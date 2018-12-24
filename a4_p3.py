# 350111
# a4_p3.py
# Amish Kapri
# a.kapri@jacobs-universty.de

Data = ("Python is a great programming language !")
print(Data)
b = Data.upper()
print(b)
word = Data.split(' ')
for i, word in enumerate(word):
    if 'programming'==word:
        print("The position of the word programming is", i+1 ,".")
e = Data.replace('!','?')
print(e)
