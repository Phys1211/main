# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:14:36 2024

@author: tomke
"""
import numpy as np
k=100000
numbers = np.array(range(k))
series = (-1)**numbers/(2*numbers+1)

tot = 4*sum(series)
print(tot)