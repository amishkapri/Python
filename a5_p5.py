# 350111
# a5_p5.py
# Amish Kapri
# a.kapri@jacobs-universty.de

import re
dictionary = {"merry":"god","christmas":"jul",
               "and":"och","happy":"gott",
               "new":"nytt","year":"år"}

def translate(list_en):

    translatedString = ""
    for i in list_en.split(" "):

        if (str(dictionary.get(i))) != "None":
            translatedString = translatedString+str(dictionary.get(i))+" "
        else:
            translatedString = ""
            return translatedString

    return translatedString


list_en = "merry christmas and happy new year"

if (translate(list_en)) == "":
    print("The sentence can not be translated")
else:
    print("The sentence in Swedish:")
    print(str(translate(list_en)))
