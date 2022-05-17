#-------------------------------------------------------------------------------
# Name:        longestWord
# Purpose:
#
# Author:      Roman Vit. Zaytsev
#
# Created:     22.10.2021
# Copyright:   (c) rzaytsev 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

str = input ("Введи любую фразу: ")
l = 0
w = ''
for word in str.split(" "):

    if len(word) > l:
        w = word
        l = len(word)

print(w)