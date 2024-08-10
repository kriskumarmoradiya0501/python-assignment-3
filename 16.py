# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:51:02 2024

@author: 8student4
"""

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(list1)

n = int(input("Enter number of index where you want to add element : "))
m = input("Enter value : ")
list1.insert(n,m)
print(list1)