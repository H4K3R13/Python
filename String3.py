# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:50:43 2021

@author: Arjun C
"""
s="I Love My Country"
x=s.split('My') # Splits the string at the specified separator, and returns a list
print(x)
x=s.split('M')
print(x)

print(s.index("M")) #Searches the string for a specified value and returns the position of where it  was found

print(s.rindex('Love'))