# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:48:57 2018

@author: Tom K
"""
import numpy as np
import math as mh

def feven(ilist):
    # takes a list of numbers
    a = list(filter(lambda x: x%2==0,ilist))
    print(a)
    return a

def fpass(func,a,b):
    # takes a function and 2 numbers a,b
    return func(a) - func(b)

def fmap(func,ilist):
    #takes a function and a list of numbers
    a=list(map(func,ilist))
    print(a)
    return(a)
    
def fsum(*args):
    #an example of a function that can take any number of arguments
    m = 0
    for arg in args:
        m +=arg
    return m

def fmany(*args):
    print('You have entered:')
    for arg in args:
        print(arg,'\n')
    return args

def fdict(**diction):
    #you will often see the input written as **kwargs in other documentation
    #diciton is a dictionary
    #sample input: a = [1,2,3], b=[3,2,1], action='cross'
    for key, values in diction.items():
        print(key,'=', values)
    a = np.array(diction['a'])
    
    if diction['action'] == 'magnitude':
        product = mh.sqrt(sum(pow(element,2) for element in a))
    elif diction['action']=='dot':
        # dot product code
        b = np.array(diction['b'])
        product = np.dot(a,b)
        
    
    elif diction['action']=='cross':
        # cross product section
        b = np.array(diction['b'])
        product = np.cross(a,b)

    else:
        print('Incorrect input')
    return product
        
        
        