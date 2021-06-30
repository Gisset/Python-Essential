# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:11:26 2021

@author: Gissela
"""
lista1=[]
lista2=[]
lista3=[]

lista=["R1","R2","R3",
       "S1","S2", "AP",
       "AP2","AP3"]
for puntero in lista:
    if "R" in puntero:
     lista1.append(puntero)      
for clave in lista:
     if "S" in clave:
       lista2.append(clave)    
for contador in lista:
     if "A" in contador:
      lista3.append(contador)   
    
print(lista1)   
print(lista2)
print(lista3)   
    
 
