#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:54:16 2021

@author: student
"""

print("While Loop")
i=1
count=0
while i%2!=0:
    print(i)
    count=count+1
    i=i+2
    if count==100:break

print("For Loop")
count=0
for i in range(1,500):
    if i%2!=0:
        print(i)
        count=count+1
        if count==100:break
    