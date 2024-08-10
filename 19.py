# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:34:58 2024

@author: 8student4
"""

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list1)

for i in list1:
    if i%2!=0:
        list1.remove(i)

print("\n after removing all elments",list1)