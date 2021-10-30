#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:56:24 2021

@author: AC
"""
a=[1,2,3,4]
b=['a','b','c']
c=[[1,2],[4,5]]
print("a[1]",a[1])
print("c[1]",c[1])
print("a[-1]",a[-1])

#nested list index
print("c[0][0]",c[0][0])
print("c[1][0]",c[1][0])

#list slicing with slicing operator:
print("a[1:2]",a[1:2])
print("a[1:]",a[1:])
print("a[:]",a[:])

#list is mutable
odd=[2,4,6,8]
odd[0]=1
print("odd[0]=1",odd)
odd[1:3]=[3,5]
print("odd[1:3]=[3,5]",odd)

# + operator
odd+[9,5,7]
print(odd)

#repeats the list for a given number of times
print([a,b,c]*3)

#delet list items
mylist=[10,20,30,40]
del mylist[2]
print("del mylist[2]",mylist)
del mylist[1:3]
print("del mylist[1:3]",mylist)
del mylist
# print(mylist) name 'mylist' is not defined it's deleted

#Removing an elements from the list
a=['a','b',[7,8],"apple"]
a.remove('a')
print("a.remove('a')",a)
a.pop(1)
print("a.pop(1)",a)
print("a.pop()",a.pop())
print("a.clear()",a.clear())

list1=[1,2,3,4,5,6,7]
list1[2:3]=[] #removes 2nd element
print("list1[2:3]=[]",list1)

#membership operator in and not in 
a=[1,2,3,4]
print("1 in a",1 in a)
print("1 not in a",1 not in a)

b=[5,2,7,1]
print("a.sort()",a.sort())
print("a.reverse",a.reverse())