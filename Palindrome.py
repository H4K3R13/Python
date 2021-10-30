#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:04:38 2021

@author: student
"""
s=list(input("Enter The String:").lower())
l=list(reversed(s))
if s==l:
    print("Palindronme")
else:
    print("Not Palindrome")
