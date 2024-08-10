# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:22:49 2024

@author: 8student4
"""


family_member_name = []
family_member_age = []
n = int(input("Enter the number of elements you want to add to the list: "))

for i in range(n):
    element = input(f"Enter name {i+1}: ")
    family_member_name.append(element)
    element1 = input(f"Enter age {i+1}: ")
    family_member_age.append(element1)
    

for i,j in zip(family_member_name,family_member_age):
    print(i,j)
    
    
    
n = len(family_member_age)
for i in range(n):
    for j in range(0, n-i-1):
        if int(family_member_age[j]) > int(family_member_age[j+1]):
            family_member_age[j], family_member_age[j+1] = family_member_age[j+1], family_member_age[j]
            family_member_name[j], family_member_name[j+1] = family_member_name[j+1], family_member_name[j]

for i,j in zip(family_member_name,family_member_age):
    print(i,j)