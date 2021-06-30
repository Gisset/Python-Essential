# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:45:31 2021

@author: Gissela
"""

acl= int(input("Ingrese el # de Acl")) 
if acl>=1 and acl <=99:
    print("la acl es Estandar")
elif acl>=100 and acl <=199:
    print("La ACL es Extendida")
else:
    print("El # ingresado no es de ACL")