# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 20:37:35 2024

@author: ADMIN
"""

employee = [
    ("Smit", 1001, "Manager"),
    ("Harmin", 1002, "Cleaning Staff"),
    ("Ashika", 1003, "HOD")
]

while True:
#     m = int(input("Enter Account number: "))
#     f = False
    
#     for i in range(len(employee)):
#         if m == employee[i][0]:
#             f = True
#             c = i
#             break

#     if not f:
#         print("No employee found number.")
#         continue

    print("If you want to ADD new Employee then enter 1")
    print("If you want to Remove Employee enter 2")
    print("If you want to Change name of Employee then enter 3.")
    print("If you want to Search Employee then enter 4.")
    print("If you want to Exit then enter 5.")

    n = int(input("enter Your choice: "))

    if n == 1:
        name = input("Enter employee name: ")
        id = int(input("Enter employee ID: "))
        dep = input("Enter department: ")
        employee.append((name, id, dep))
        print(f"Employee {name} added successfully.")
    elif n == 2:
        m = int(input("Enter Employee id : "))
        f = False
        
        for i in employee:
            if m == i[1]:
                employee.remove(i)
                f = True
                c = i
                break
        if not f:
            print("employee not found")
            
    elif n == 3:
        m = int(input("Enter Employee id to change name : "))
        n_name = input("Enter new name :")
        f = False
        l=0
        for i in employee:
            if m == i[1]:
                employee[l]=(n_name,i[1],i[2])
                print(i[0],i[1],i[2])
                f = True
                c = i
                break
            l+=1
        if not f:
            print("employee not found")
    elif n == 4:
        m = int(input("Enter Account number: "))
        f = False
        
        for i in range(len(employee)):
            if m == employee[1]:
                print(i[0],i[1],i[2])
                f = True
                c = i
                break
    elif n == 5:
        print("exit")
        break
    else:
        print("invalid input")


print(employee)