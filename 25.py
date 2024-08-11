# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:43:21 2024

@author: ADMIN
"""
id = ('24BCA001','24BCA002','24BCA003')

detail = []

for i in range(len(id)):
    print("Enter details for Student ID: ",id[i])
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    city = input("Enter Student City: ")
    
    detail.append([name, age, city])
print()
print("Student Details:")
for i in range(len(id)):
    print("Student ID:",id[i]," Student Name: ",detail[i][0]," Age: ",detail[i][1]," City: ",detail[i][2])
