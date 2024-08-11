# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 20:37:35 2024

@author: ADMIN
"""

employee = [
    (1001,"Smit" ,2.5,120000),
    (1002,"Harmin",5,10000),
    (1003,"Arshika",0.5,100000)
]

while True:

    print("If you want to ADD new Employee then enter 1")
    print("If you want to Exit then enter 2.")

    n = int(input("enter Your choice: "))

    if n == 1:
        name = input("Enter employee name: ")
        id = int(input("Enter employee ID: "))
        exp = float(input("Enter Experience: "))
        sal = float(input("Enter Salary : "))
        employee.append((name, id, exp,sal))
    elif n == 2:
        print("exit")
        break
    else:
        print("invalid input")


print()
print()
print("Updated salary is :")
print()

l=0
for i in employee:
    if i[2] > 1:
        a=i[3]
        a+=a*0.05
        employee[l]=(i[0],i[1],i[2],a)
        print(i[0],i[1],i[2],a)
        f = True
        c = i
    elif i[2] > 2:
        a=i[3]
        a+=a*0.10
        employee[l]=(i[0],i[1],i[2],a)
        print(i[0],i[1],i[2],a)
        f = True
        c = i
    elif i[2] > 3:
        a=i[3]
        a+=a*0.15
        employee[l]=(i[0],i[1],i[2],a)
        print(i[0],i[1],i[2],a)
        f = True
        c = i
    elif i[2] > 4:
        a=i[3]
        a+=a*0.20
        employee[l]=(i[0],i[1],i[2],a)
        print(i[0],i[1],i[2],a)
        f = True
        c = i
    else:
        print(i[0],i[1],i[2],i[3])
    l+=1

