#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rzaytsev
#
# Created:     19.03.2022
# Copyright:   (c) rzaytsev 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

#-- Строки: функция .format
# Задачи:
#	- распечатать кассовый чек, где все строки текста находится посредине.
#	- распечатать число 1/7 с точночтью до 14 знаков
#	- прочитать строку/список наоборот

    str = 'str'
    print(str[::-1])

    ф=1; и=2
    ф,и = и,ф
    print(ф,и)

#-- Логические операции:
    print(~~True); print(not True); print(not not True)
    print(~~False)
    print(False & True)
    print(False | True)

    print(0|True)
    print(1|True)
    print(2|True)
    print(3&True)

    print(False==0)
    print(True==1)

    print(False == True + ~False)
    print(False + True == False - ~False)
    print(~False == ~True - ~False)
    print(~True==~False + False + ~False)
    print(~False&~True == ~True)
    print(False == True + ~False)

#-- Операции
    print(1**-1)
    print(1**0)
    print(0**10)
    print(0**0)
    print(1+2*0**-0/~True)

#-- Порядок операций
    print(1+2*0**-0/~True)

#-- Функции и передача параметров
# Какой результат выполнения блока команд
    def func(x):
        x = 2
    x=50; func(x)
    print(x)

# Какой результат выполнения блока команд
    def changeList(list):
        list.append(3)
    list = [1,2]
    changeList(list)
    print(list)


#-- Операции над списками

# Какой результат выполнения блока команд
    bmw = ['M8', 'X5', 'Z4']
    cars = bmw
    cars.append('CHEROKEE')
    print('All cars: ', cars)
    print('bmw: ', bmw)

# Какой результат выполнения блока команд
    cars = ['CHEROKEE', 'M8', 'X5', 'Z4']
    bmw = cars
    bmw.remove('CHEROKEE')
    print('All cars: ', cars)
    print('bmw: ', bmw)

# Какой результат выполнения блока команд
    cars = ['CHEROKEE', 'M8', 'X5', 'Z4']
    bmw = cars[1:]
    print('All cars: ', cars)
    print('bmw: ', bmw)


#-- Операции над множествами

# Какой результат выполнения блока команд
    cars = set(['CHEROKEE', 'M8', 'X5', 'Z4'])
    bmw =  set(['8 SERIES', 'M8', 'X5', 'Z4'])
    print('cars & bmw: ', cars & bmw)
    print('cars | bmw: ', cars | bmw)
    print('cars ^ bmw: ', cars ^ bmw)
    print('bmw ^ cars: ', bmw ^ cars)

#-- Классы
'''
Написать класс Car, включающий данные о машине:
  - фирма-производитель
  - марка машины
  - год выпуска машины
  - цена
  - цвет

Для класса машин написать функцию печати содержимого полей класса
в формате json-строки вида:
    {имя_поля_1:значение_поля_1, имя_поля_2:значение_поля_2, ....}

Создать список машин, имеющихся на складе и отсортировать:
    - по дате выпуска машины
    - по стоимости по возрастанию и убыванию цены
    - по цвету
'''


if __name__ == '__main__':
    main()
