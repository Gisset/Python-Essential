# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:16:24 2021

@author: Gissela
"""

def is_prime(num):
    if num<2:# La variable es mayor a dos 
        return False# retorne falso.  
    elif num == 2:
        return True
    for n in range(2,num):
        if num % n == 0:
            return False
        return True
    
       
print(is_prime(6))
for i in range(1,20):
     if is_prime(i+1):
        print(i+1,end="")
print()
           