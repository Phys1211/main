# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:27:31 2016
Function used to determine if a module contains a given function. 
@author: Tom
"""
def qcount(mod, func):
    '''
    Parameters
    ----------
    mod : module name
    
    func : string
        function name.

    Returns
    -------
    counter : number of times func appears in module

    '''
    a = dir(mod)
    r = range(len(a))
    counter = 0
    for i in r:
        if a[i]==func:
            counter += 1
    #print(a)        
    return counter

def qcontain(mod, func):
    #checks for func in module mod
    return func in dir(mod)

if main == '__main__':
    