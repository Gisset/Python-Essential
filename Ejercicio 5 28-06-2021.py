# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:33:11 2021

@author: Gissela
"""
def saludo2(nombre1,nombre2):
    print("Hola",nombre1)
    print("Hola",nombre2,"\n")
    
saludo2("Juan","Carlos")
saludo2("Ana","Carlos")
saludo2("Israel","Julian")


def direct(calle,codigopostal,ciudad):
    print("Su direccion es: \nCiudad", ciudad)
    print("La calle es: \nCalle", calle)
    print("Su codigo postal es: \tcodigo postal",codigopostal)
    
print("Ingrese los siguientes datos")
cl=input("Ingrese la calle:")
cu=input("Ingrese la ciudad:")
cp=input("Ingrese el codigo postal:")     