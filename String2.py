# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:44:00 2021

@author: Arjun C
"""
s="I Love My Country"
#center(width,fillchar)  Returns a centered string
print(s.center(100,'+'))
print(s.center(20,'*'))

 #count(text,start [int],end[int]) Returns the number of times a specified value occurs in a string
print(s.count('t'))
print(s.count('t',2 ))
s1="this is counting this"
print(s1.count('this' ))
print(s1.count('t',2 ))
print(s1.count('t',2,13))
print(s.endswith('Country'))
print(s.endswith('string'))
