#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rzaytsev
#
# Created:     11.11.2021
# Copyright:   (c) rzaytsev 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

phrase = "Затем идут несколько     пробелов"

def reduce(s = "    "):
    ss = s.replace("  ", " ")
    if len(s) == len(ss):
        return s
    else:
        return reduce(ss)

print(reduce(phrase))

def reduceSpace(s = "   "):
    ss = s.replace("  ", " ")
    while len(s) != len(ss):
        s, ss = ss, ss.replace("  ", " ")
    return ss

print(reduceSpace(phrase))

#--- функция нормализации строки
def normalize(frase):
    return frase.lower().replace(',','').replace('!','').replace('.','').replace(':','').replace('-','').replace('"','').replace("'","")

#--- Модификация Алгоритма №4
def uniqueWords(str):
    words = reduceSpace(normalize(str)).split(' ')
    dict = {}
    for word in words:
        if(dict.get(word) == None):
            dict[word] = sum(1 for w in words if w == word)
    return dict


