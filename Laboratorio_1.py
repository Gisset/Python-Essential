# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:01:37 2021

@author: Gissela
"""
"""x=float(input("Ingrese :"))
z= float(235.21) 
y= z/x
print(y)"""

def l100kmtompg(liters):
    y=(100/((liters *  1609.344)/ 3.785411784))*1000 #<float(235.21)/liters
    print("\t", "El resultado en l/km es:",y,"\n")

def mpgtol100km(miles):
    x=((3.785411784 * (100 / miles)) / 1609.344)*1000 #float(235.21)/miles
    print("\t", "El resultado en mpg es:",x,"\n")

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))