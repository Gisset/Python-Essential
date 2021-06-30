# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:44:08 2021

@author: Gissela
"""
while True:
    x=input("Ingrese el numero a contar hasta:")
    if x=="q" or x=="quit":
       break
    
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1  
        if y>x:
            break