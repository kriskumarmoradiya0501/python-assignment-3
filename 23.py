# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:25:02 2024

@author: ADMIN
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:14:02 2024

@author: ADMIN
"""

completed = []
pending = []

while True:

    print("If you want to add completed task then enter 1")
    print("If you want to add pending task then enter 2")
    print("If you want to display pending and completed task then enter 3")
    print("If you want to Exit then enter 4.")

    n = int(input("enter Your choice: "))

    if n == 1:
        index = int(input("Enter index for completed task: "))
        task = input("Enter name of completed task")
        completed.append((index,task))
        print(index,task," is added.")
    elif n == 2:
        index = int(input("Enter index for pending task: "))
        task = input("Enter name of pending task")
        pending.append((index,task))
        print(index,task," is added.")    
    elif n == 3:
        print(completed)
        print()
        print()
        print(pending)
    elif n == 4:
        print("exit")
        break
    else:
        print("invalid input")


