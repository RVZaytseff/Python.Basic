#-------------------------------------------------------------------------------
# Name:        multiplyTable
# Purpose:
#
# Author:      Roman Zaitsev
#
# Created:     22.10.2021
# Copyright:   (c) rzaytsev 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

M = int(input ("Введи число M: "))
a = int(input ("Введи число a: "))
b = int(input ("Введи число b: "))
i = a
while i in range(a, b):
     print (i, ' * ', b, ' = ', i*b)
     i += 1
