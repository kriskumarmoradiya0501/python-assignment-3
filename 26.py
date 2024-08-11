# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:56:06 2024

@author: ADMIN
"""

users = [
    [1001,'ramesh',['Feb-2024',1200],['May-2024',1550]],
    [1002,'suresh',['Feb-2024',1500],['May-2024',1650]],
    [1003,'jayesh',['Feb-2024',1800],['May-2024',2000]]
]

rate = 5  
for user in users:
    if user[0] == 1001:
        user.append(['July-2024',2020])
    elif user[0] == 1002:
        user.append(['July-2024',2200])
    elif user[0] == 1003:
        user.append(['July-2024',2400])

for user in users:
    id = user[0]
    name = user[1]
    feb = user[2][1]
    may = user[3][1]
    july = user[4][1]
    
    feb_may =may-feb
    may_july =july-may
    
    units = feb_may + may_july
    bill = units * rate
    
    print("Account Number: ",id)
    print("Name: ",name)
    print("Reading in Feb-2024: ",feb," units")
    print("Reading in May-2024: ",may," units (Usage: ,",feb_may," units)")
    print("Reading in July-2024: ",july," units (Usage: ",may_july," units)")
    print("Total Units Used: ",units,"units")
    print("Total Bill Amount: ",bill)
    print()
    print()