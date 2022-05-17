#-------------------------------------------------------------------------------
# Name:        repeatable
# Purpose:     Этот безумный безумный безумный мир
#
# Author:      Roman Vit. Zaytsev
#
# Created:     23.10.2021
# Copyright:   (c) rzaytsev 2021
#-------------------------------------------------------------------------------

import recursion

str = 'ЭТОТ прекрасный и такой безумный, безумный, безумный  мир!'
print(str)

###-- Алгоритм №1
##words = []
##for word in str.split(' '):
##    exclude = True
##    for w in words:
##        if(w == word):
##            exclude = False
##    if(exclude):
##        words.append(word)
##
##print(words)
##
###--- Алгоритм №2
##words = str.split(' ')
##for word in words:
##    for w in words[words.index(word) + 1:]:
##        if(w == word):
##            del words[words.index(w)]
##print(words)
##

#--- Алгоритм №3
#print(set(str.split(' ')))


#--- Алгоритм №4
words = str.split(' ')
dict = {}
for word in words:
    if(dict.get(word) == None):
        dict[word] = 1
    else:
        dict[word] += 1 #  dict[word] =  dict[word] + 1

print(dict.keys())
print(dict.values())
print(dict)

#--- Модификация Алгоритма №4

#--- функция нормализации строки
def normalize(frase):
    return frase.lower().replace(',','').replace('!','').replace('.','').replace(':','').replace('-','')

def uniqueWords(str):
    words = recursion.reduceSpace(normalize(str)).split(' ')
    dict = {}
    for word in words:
        if(dict.get(word) == None):
            dict[word] = sum(1 for w in words if w == word)
    return dict

print(uniqueWords(str))




