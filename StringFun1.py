#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:55:15 2021

@author: student
"""

txt="hello, and welcome to my world"
x=txt.capitalize()
print(x)

#Placeholder,Format function
txt1="My name is {fname},I'm {age}".format(fname='Jhon',age=36)
txt2="My name is {0},I'm {1}".format("Jhon",36)
txt3="My name is {},I'm {}".format("Jhon", 36)
print(txt1)
print(txt2)
print(txt3)