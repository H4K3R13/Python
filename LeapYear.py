#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:02:01 2021

@author: student
"""

year=int(input('Enter Year:'))
if year%100==0:
    if year%400==0:
        print("Leap year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not Leap")