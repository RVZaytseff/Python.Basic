#-------------------------------------------------------------------------------
# Name:        file Operations
# Purpose:
#
# Author:      Roman Vit. Zaytsev
#
# Created:     12.11.2021
# Copyright:   (c) rzaytsev 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wordsLibrary

phrase = 'ЭТОТ жестокий - такой безумный, безумный, безумный  мир!  - Затем идут несколько     пробелов'

dict = wordsLibrary.uniqueWords(phrase)

file_name = "Частота повторения слов.txt"

fr = open(file_name, "r") # read
print("file.mode: ", fr.mode)
print("file.name: ", fr.name)
text = fr.read()
print(text)
fr.close()
print('file.closed: ', fr.closed)

fw = open(file_name, "a") # a - add - добавить,  w - write
fw.write("Фраза: '" + phrase + "'" + "\n" )
for word, quantity in dict.items():
    fw.write(word + " : " + str(quantity) + "\n")

fw.close()
pass

with open(file_name, "a") as fw:
    fw.write("Фраза: '" + phrase + "'" + "\n" )
    for word, quantity in dict.items():
        fw.write(word + " : " + str(quantity) + "\n")

file_name = "Частота повторения лов.txt"

try:
    with open(file_name, "r") as fr:
        text = fr.read()
        print(text)
except Exception as e:
    print('Файл ' + fr.name + ' не открывается: проверьте название файла и его расположение ')
    print(e)

