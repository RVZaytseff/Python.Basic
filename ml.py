#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Roman Vit. Zaytsev
#
# Created:     12.11.2021
# Copyright:   (c) rzaytsev 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Проерка версий библиотек
# Версия Python
import sys
print('Python: {}'.format(sys.version))

# Загрузка scipy
import scipy
print('scipy: {}'.format(scipy.__version__))

# Загрузка numpy
import numpy
print('numpy: {}'.format(numpy.__version__))

# Загрузка matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

# Загрузка pandas
import pandas
print('pandas: {}'.format(pandas.__version__))

# Загрукзка scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

print(dataset)