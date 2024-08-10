# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:20:30 2024

@author: 8student4
"""

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(list1)

n = int(input("Enter number : "))
c=0
for i in list1:
    if i == n :
        c +=1
        print(n," is found at ",i,"index")
        break

if c ==0:
    list1.append(n)
print(list1)
    