# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:59:07 2024

@author: 8student4
"""

list1=[1,2,3,4,5,6,7,8,9,10]

n = int(input("Enter Number to check : "))

for i in list1:
    if n == i:
        print("Number ",n,"is Found on",i,"th index")
        break;
