#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 11:14:24 2022

@author: student
"""

import random
def hint1(g,b):
    if(b>g):
        print("your guess is less than the actual no.")
    else:
        print("your guess is greater than the actual no.")
l=[10,50,8,5,66,34,77,1]
b=random.choice(l)

print(l)
i=5
while(i>0):
    g=int(input("Guess the number: "))
    if(g==b):
        print("Correct!!!")
        break
    else:
        hint1(g,b)
        
    i=i-1
if(i==0):
    print("GAME OVER!! Correct answer is ",b)