# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:24:20 2021

@author: Gissela
"""
def isYearLeap(year):
    if year % 4 != 0: #no divisible entre 4
        return True
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 100 y no entre 400
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
         return True
     
        
def daysInMonth(year, month):
    # Abril, junio, septiembre y noviembre tienen 30
    if month in [4, 6, 9, 11]:
        print ("El mes",month,"tiene: 30")
        return
    # Febrero depende de si es o no bisiesto
    if month == 2:
        if isYearLeap(year):
            print ("29")
            return
        else:
            print ("28")
            return
    else:
        # En caso contrario, tiene 31 días
        print ("31")
        return
year=int(input(" Ingrese año:"))
month=int(input(" Ingrese mes:"))
daysInMonth(year,month)

                
                