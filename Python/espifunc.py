# -*- coding: utf-8 -*-
"""
Created on ...

@author: ...
Description: ...
    
"""
import numpy as np

def main():
    #Program body
    k = int(input("Enter the number of terms to sum: "))
    r = range(k)
    karray = np.array(r)
    estpi = 4*(-1)**(karray)/(2*karray+1)
    estpi = sum(estpi)
    print("My estimate for pi is",estpi)
    return estpi
    
#The code below runs whatever is in main()
if __name__ == '__main__':
    main() 