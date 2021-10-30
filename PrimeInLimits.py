#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:47:45 2021

@author: student
"""

l1=int(input("Enter l1:"))
l2=int(input("Enter l2:"))
for num in range(l1,l2):
    count=0
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if(count==2):
        print(num)