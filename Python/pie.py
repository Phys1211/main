# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:11:01 2024

@author: tomke
"""

import numpy as np
import matplotlib.pyplot as plt
import random
def piestimator(num_points = 1000):
 
    #Initialize count of points inside the quarter circle
    inside_circle = 0
    
    
    #Turn on interactive mode
    plt.ion()  
    #Initialize plot
    fig, (ax_main, ax_pi) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1], 'hspace': 0.5})
    ax_main.set_aspect('equal')
    ax_main.set_xlim([0, 1])
    ax_main.set_ylim([0, 1])
    ax_main.set_title('Estimating Pi')
    
    # Initialize lists to store x and y coordinates of points inside and outside the circle
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    
    # Initialize list to store running estimates of pi
    pi_estimates = []
    
    # Generate random points and check if they are inside the quarter circle
    for i in range(num_points):
        #Random x-coordinate in the range [0, 1]
        x = random.uniform(0, 1) 
        #Random y-coordinate in the range [0, 1]
        y = random.uniform(0, 1) 
        # Distance from the origin
        distance = x**2 + y**2 
        #Check if the point is inside the quarter circle (x^2 + y^2 <= 1)
        if distance <= 1:          
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
        
        #Estimate the value of pi
        pi_estimate = 4 * inside_circle / (i + 1)
        pi_estimates.append(pi_estimate)
    
        # Plot points on square
        ax_main.clear()
        ax_main.set_aspect('equal')
        ax_main.set_xlim([0, 1])
        ax_main.set_ylim([0, 1])
        ax_main.set_title(f'Estimating Pi: {pi_estimate:.6f}')
        ax_main.scatter(x_inside, y_inside, color='blue', marker='.')
        ax_main.scatter(x_outside, y_outside, color='red', marker='.')
        
        # Plot pi estimate line
        ax_pi.clear()
        ax_pi.plot(pi_estimates, color='green')
        ax_pi.axhline(y=np.pi, color='red', linestyle='--', label='True Pi')
        ax_pi.set_title('Pi Estimate')
        ax_pi.set_xlabel('Number of Points')
        ax_pi.set_ylabel('Pi Estimate')
        ax_pi.legend()
        
        plt.draw()
        plt.pause(0.001)
    # Turn off interactive mode after the loop
    plt.ioff()  
    plt.show()
    return pi_estimate

if __name__ == '__main__':
    piestimator(100)