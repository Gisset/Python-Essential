# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:20:39 2021

@author: Gissela
"""

contar=input("Ingrese el # al que debo contar")
contar=int(contar)
contador=1
while contador<=contar:
    print(contador)
    contador+=1
    print("dentro de while")
print("fuera de while")
