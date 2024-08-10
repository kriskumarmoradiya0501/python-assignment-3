# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:19:34 2024

@author: 8student4
"""
list1 = []

n = int(input("Enter the number of elements you want to add to the list: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list1.append(element)
print("The list is:", list1)


    
