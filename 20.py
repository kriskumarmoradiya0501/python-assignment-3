# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:39:23 2024

@author: 8student4
"""
list1 = [[1001,'account1',5000],[1002,'account2',5000],[1003,'account3',5000]]

while True:
    m = int(input("Enter Account number: "))
    f = False
    
    for i in range(len(list1)):
        if m == list1[i][0]:
            f = True
            c = i
            break

    if not f:
        print("invlid account number.")
        continue

    print("If you want to deposit the money then enter 1")
    print("If you want to withdraw then enter 2")
    print("If you want to end the task then enter 3.")
    n = int(input("enter Your choice: "))

    if n == 1:
        a = int(input("enter Your Amount of deposit: "))
        list1[c][2] += a
        print("new balance for account ",m," : ",list1[c][2])
    elif n == 2:
        a = int(input("enter Your Amount of withdrawal: "))
        if a > list1[c][2]:
            print("Your account has not that much money")
        else:
            list1[c][2] -= a
            print("new balance for account",m,": ",list1[c][2])
    elif n == 3:
        print("exit")
        break
    else:
        print("invalid input")
