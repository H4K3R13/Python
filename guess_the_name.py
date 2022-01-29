#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 11:27:59 2022

@author: student
"""

import random
l=["amal","arju","dev","vishnu","sibi","akash","hari","anjana","rarika","gopika"]
b=random.choice(l)
i=3
print(l)
while(i!=0):
    g=input("Guess the name: ")
    g.lower()
    if(g==b):
        print("Your Guess is correct")
        break
    else:
        if i==3:
            print("First  Letter is ",b[0])
        elif i==2:
            print("Last letter:",b[-1])
        elif i==1:
            print("Lenght is",b.count)
    i=i-1
if i==0:
    print("GAME OVER!! Correct Name: ",b)

