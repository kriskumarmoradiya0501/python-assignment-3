# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:14:02 2024

@author: ADMIN
"""

grocery = []


while True:

    print("If you want to ADD new item then enter 1")
    print("If you want to Remove item then enter 2")
    print("If you want to display items then enter 3")
    print("If you want to Exit then enter 4.")

    n = int(input("enter Your choice: "))

    if n == 1:
        name = input("Enter name of item: ")
        id = int(input("Enter id of item: "))
        dep = float(input("Enter Quantity of item: "))
        grocery.append((name, id, dep))
        print(name,id,dep," is added.")
    elif n == 2:
        m = int(input("Enter id of item : "))
        f = False
        
        for i in grocery:
            if m == i[1]:
                grocery.remove(i)
                f = True
                c = i
                break
        if not f:
            print("item id is not found")
            
    elif n == 3:
        print(grocery)
    elif n == 4:
        print("exit")
        break
    else:
        print("invalid input")


print(grocery)