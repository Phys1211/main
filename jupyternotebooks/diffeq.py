# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:42:19 2018

@author: Tom K
"""
from numpy import arange
import matplotlib.pyplot as pyl

def rk2(func,a=0,b=10,N=100):
    # Takes a lambda function and limits of the solution requested. Solves Diffeq using 2nd order Runga-Kutta method
    h = (b-a)/N

    tpoints = arange(a,b,h)
    xpoints = []
    #sets initial condition
    x = 0.0
    for t in tpoints:
        xpoints.append(x)
        k1 = h*func(x,t)
        k2 = h*func(x+0.5*k1,t+0.5*h)
        x += k2
    #plots solution
    pyl.plot(tpoints,xpoints)
    pyl.xlabel("t")
    pyl.ylabel("x(t)")
    pyl.show()
    return xpoints

def rk4(func,a=0,b=10,N=100):
    # Takes a lambda function and limits of the solution requested. Solves Diffeq using 2nd order Runga-Kutta method
    h = (b-a)/N

    tpoints = arange(a,b,h)
    xpoints = []
    #sets initial condition
    x = 0.0
    for t in tpoints:
        xpoints.append(x)
        k1 = h*func(x,t)
        k2 = h*func(x+0.5*k1,t+0.5*h)
        k3 = h*func(x+0.5*k2,t+0.5*h)
        k4 = h*func(x+k3,t+h)
        x += (k1+2*k2+2*k3+k4)/6
    #plots solution
    pyl.plot(tpoints,xpoints)
    pyl.xlabel("t")
    pyl.ylabel("x(t)")
    pyl.show()
    return xpoints
