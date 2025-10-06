# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:28:03 2019

@author: Tom K
"""
import numpy as np
import matplotlib.pyplot as pyp
# Defining Constants
G = 6.67*10**(-11);
M = 5.98*10**(24);
R = 6.371*10**(6);
#Take input


def altitude(T):
    h=(G*M*T**2/(4*np.pi**2))**(1/3) - R;
    h = h/1000
    return h
def velo(h):
    v = np.sqrt(G*M/(h+R))
    v=v/1000
    return v

if __name__ == '__main__':
    T = input("Input the bodys orbital period around the Earth (in sec): ")
    T = float(T)
    h = altitude(T)
    v = round(velo(h),1)
    print(f'The satellite orbits at a altitude of {h} km and at {v} km/s.')
