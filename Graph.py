#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:39:13 2021

@author: student
"""

from turtle import *
color('green', 'green')
begin_fill()
while True:
    forward(300)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()