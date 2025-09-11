# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 16:20:40 2025

@author: tomke
"""
import numpy as np

k = range(10000000)
k = np.array(k) 
x =  ((-1)**k)/(2*k+1)
ans = 4*np.sum(x)
print(ans)