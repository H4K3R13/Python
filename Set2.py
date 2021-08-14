# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:16:58 2021

@author: Arjun C
"""

#add() Adds an element to the set
MySet=set({'India','Kerala','Kannur','Karivellur'})
MySet.add('Kasaragod')
print("Kasaragod is added:",MySet)

 #copy() Returns a copy of the set
NewSet=MySet.copy()
print("Copy of the set is :" ,NewSet)

 #difference() Returns a set containing the difference between two or more sets
Districts=set({'Kannur','Kasaragod'})
x= MySet.difference(Districts)
print("Set Difference", x)
y=Districts.difference(MySet)
print(y)

