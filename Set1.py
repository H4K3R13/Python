# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:03:17 2021

@author: Arjun C

"""
#Creating A Set
set1=set()
print("Initial blank Set:")
print(set1)

#Creating a Set with the use of a string
set2=set("India is my Country")
print("\nSet with the use of String:")
print(set2)

 # Creating a Set with the use of a List
set3 = set(["India", "Kerala", "Kannur"])
print("\nSet with the use of List: ")
print(set3)

#Using loop to access elements
print("\nElements of set: ")
for i in set3:
 print(i, end =" ")
 
 #Checking Elements
print("\nIndia" in set3)

