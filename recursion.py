#-------------------------------------------------------------------------------
# Name:        Recursion
# Purpose:
#
# Author:      Roman Vit. Zaytsev
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

