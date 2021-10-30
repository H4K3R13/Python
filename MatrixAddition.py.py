#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:06:36 2021

@author: student
"""

# Program to add two matrices using nested loop

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]

result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

for i in range(len(X)):
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j] #Addtion

for r in result:
	print(r)
 