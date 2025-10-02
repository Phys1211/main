# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:28:03 2019

@author: Tom K
"""
import numpy as np
import matplotlib.pyplot as pyp

G = 6.67*10**(-11);
M = 5.98*10**(24);
R = 6.371*10**(6);

T = input("Input the bodys orbital period around the Earth (in sec): ")


h=(G*M*T**2/(4*np.pi**2))**(1/3) - R;
v = np.sqrt(G*M/(h+R))
v=v/1000
h=h/1000
print('The satellite orbits at a altitude of {0:.1f} km and at {1:.1f} km/s.'.format(h,v))
