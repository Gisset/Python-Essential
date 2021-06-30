# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:42:52 2021

@author: Gissela
"""

lista1= ["Juan",5,5.7,True,5]
print(type(lista1))
print(len(lista1))
tupla1=("Juan",5,5.7,False,5,True)
print(type(tupla1))
print(len(tupla1))
print(lista1[0],"\n")
print(lista1[1],"\n")
print(lista1[2],"\n") 
print(lista1[-1],"\n") 
print(lista1[-5],"\n")
print(lista1[2],"\n")
print(lista1[0],"\n")
lista1[1]="Carlos"
print(lista1)
tupla1[0]="R2"
print(tupla1)
del tupla1[0]

