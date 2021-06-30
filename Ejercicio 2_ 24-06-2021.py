# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 20:17:35 2021

@author: Gissela
"""

dict1={"R1": "10.10.0.1",
       "R2":"10.10.0.",
       5:"1713151414",
       "juan":"0999999999",
       "ID1":52.5,
       "ID2":8, 
       "R3":"10.0.0.1"}

print(dict1,"\n"*2)
print(dict1["R1"])
dict1["S1"]="10.1.1.1"
dict1["AP1"]="10.10.10.1"
dict1["AP2"]="10.10.10.1"
dict1["AP2"]="10.10.10.11"
"10.10.10.1" in dict1
del dict1[5]
del dict1[6]
