#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:06:34 2021

@author: student
"""
punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s=input("Enter The String:")
for i in s:
    if i in punc:
        s=s.replace(i,"")
print(s)



