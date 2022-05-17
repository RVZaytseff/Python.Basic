#-------------------------------------------------------------------------------
# Name:        logging & exceptions
# Purpose:     learning about function and exception from normal execution
#
# Author:      Roman Vit. Zaytsev
#
# Created:     06.11.2021
# Copyright:   (c) rzaytsev 2021
#-------------------------------------------------------------------------------


def increment(x):
    return x + 1

print (increment(1))

#-
def increment(x=0):
    return x + 1

print (increment(2))
print (increment())

#--

increment = lambda x: x + 1

print (increment(1))

#---
def logging(func, args):
    res = func(args)
    print ('calling %s, input parameter = %s returned = %s' % (func.__name__, args, res))
    return res

def double(x):
    y = 2*x
    print("Doubles of number %s equals %s" %(x,y))
    return y

if __name__ == '__main__':
   print (logging(double, 155))

#----
# Исключения
# Исключения в Python имеют структуру try-except [exceptionname]
devide = lambda x,y: x/y

def division(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        # Но программа не "Выполняет недопустимую операцию"
        # А обрабатывает блок исключения соответствующий ошибке «ZeroDivisionError»
        print ("Ошибка: Деление на ноль")
        return None

print (devide(10, 7))
print (division(10, 3))
print (division( 1, 0))