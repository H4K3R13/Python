#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:49:03 2022

@author: AC
"""

import pandas as pd
import numpy as np

# Summarise and Computing, Descriptive Statistics
df=pd.DataFrame([[1.4,np.NaN],[7.1,-4.5],[np.NaN,np.NaN],[0.75,-1.3]],
                 index=['A','B','C','D'],columns=['One','Two'])
print("\n Printing DF:\n",df)
print("\n df.sum()\n",df.sum())
print("\n df.sum(axis=1)\n",df.sum(axis=1)) 
