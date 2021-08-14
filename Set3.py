# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:24:45 2021

@author: MADHUPRAJITHA
"""

 #discard()Remove the specified item
MySet=set({'India','Kerala','Kannur','Karivellur'})
MySet.discard('India')
print("Removes India:", MySet) 

#intersection() Returns a set, that is the intersection of two or more sets
Districts=set({'Kannur','Kasaragod'})
x= MySet.intersection(Districts)
print("Intersection is: ",x)

 #isdisjoint() Returns whether two sets have a intersection or not
x=MySet.isdisjoint(Districts)
print("Is Disjoint:", x)
print(MySet)
print(Districts)

#difference_update() Removes the items in this set that are also included in another, specified set
MySet.difference_update(Districts)
print(MySet)

#intersection_update() Removes the items in this set that are not present in other,  specified set(s)

x=set({1,2,3,4,5})
y=set({1,2,3})
x.intersection_update(y)
print(x)

#clear() Removes all the elements from the set
x.clear()
print(x)
