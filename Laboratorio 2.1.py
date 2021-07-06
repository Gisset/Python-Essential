# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:57:57 2021

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
x=int(input("Ingrese :"))
print(isYearLeap(x))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            if result == testResults[i]:
                        print("OK")
            else:
                        print("Failed")