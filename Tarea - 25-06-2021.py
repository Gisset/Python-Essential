# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:29:54 2021

@author: Gissela
"""
"Ingrese su información"

#nombre=input("Ingrese su Nombre:")
#Apellido=input("Ingrese su Apellido:")
#Edad=int(input("Ingrese su edad:"))
#Direccion=input("Ingrese su direccion:")

#space=""


#print("Sus datos son", {nombre})
nombre = input("Ingrese su Nombre:")
apellido=input("Ingrese su Apellido:")
edad=int(input("Ingrese su edad:"))
dire =input("Ingrese su direccion:")

print("\n"*2,"Su información se encuentra registrada","\n"*1) 
print(" verifique por favor","\n"*2)

space=" "
print("Sus datos son:"+space+nombre+space+apellido)
print("Usted tiene:",edad,"años")
print("vive en :"+space+dire)
