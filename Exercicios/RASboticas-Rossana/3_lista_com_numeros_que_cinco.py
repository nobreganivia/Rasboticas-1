# -*- coding: utf-8 -*-
"""3 - Lista com numeros que cinco.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G6jmAo_7VfgqO8pyqPyKemY2U-Kxzn3a
"""

x = [1, 2, 2, 3, 4, 5, 13, 21, 34, 55, 89] #imprima em uma nova lista os valores menores que 5
a = []

for i in x:
  if i <5:
    a.append(i)
print (a)