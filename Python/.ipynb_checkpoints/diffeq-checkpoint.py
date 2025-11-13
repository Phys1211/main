# -*- coding: utf-8 -*-
"""
ODE Solvers for Computational Physics
Created on Fri Sep 21 16:42:19 2018
Updated: 2025

@author: Tom K

This module provides numerical ODE solvers using Euler, RK2, and RK4 methods.
Functions come in two flavors:
1. Single-step functions (euler_step, rk2_step, rk4_step) - for manual time-stepping
2. Complete solver functions (euler, rk2, rk4) - for automatic solving over an interval
"""

import numpy as np
import matplotlib.pyplot as plt



# ============================================================================
# SINGLE-STEP FUNCTIONS (for use in manual time-stepping loops)
# ============================================================================

def euler_step(y, f, t, dt):
    """
    Take one Euler method step for dy/dt = f(t, y)
    
    Parameters
    ----------
    y : float or array
        Current value of dependent variable
    f : function
        Right-hand side function f(t, y) that returns dy/dt
    t : float
        Current time
    dt : float
        Time step size
        
    Returns
    -------
    float or array
        Updated value: y_new = y + f(t, y)*dt
        
    Example
    -------
    >>> def cooling(t, T):
    ...     return -0.1 * (T - 20)
    >>> T = 90.0
    >>> T_new = euler_step(T, cooling, 0.0, 0.1)
    """
    return y + dt * f(t, y)


def rk2_step(y, f, t, dt):
    """
    Take one RK2 (midpoint method) step for dy/dt = f(t, y)
    
    Parameters
    ----------
    y : float or array
        Current value
    f : function
        Right-hand side function f(t, y)
    t : float
        Current time
    dt : float
        Time step
        
    Returns
    -------
    float or array
        Updated value using RK2 midpoint method
        
    Notes
    -----
    RK2 achieves O(dt²) global error by sampling the slope at the midpoint.
    """
    k1 = f(t, y)
    k2 = f(t + 0.5*dt, y + 0.5*dt*k1)
    return y + dt * k2


def rk4_step(y, f, t, dt):
    """
    Take one RK4 step for dy/dt = f(t, y)
    
    Parameters
    ----------
    y : float or array
        Current value
    f : function
        Right-hand side function f(t, y)
    t : float
        Current time
    dt : float
        Time step
        
    Returns
    -------
    float or array
        Updated value using RK4
        
    Notes
    -----
    RK4 achieves O(dt⁴) global error and is the workhorse of numerical ODE solving.
    It samples the derivative at four points: start, two midpoints, and end.
    """
    k1 = f(t, y)
    k2 = f(t + 0.5*dt, y + 0.5*dt*k1)
    k3 = f(t + 0.5*dt, y + 0.5*dt*k2)
    k4 = f(t + dt, y + dt*k3)
    return y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)


# ============================================================================
# COMPLETE SOLVER FUNCTIONS (solve entire ODE over interval)
# ============================================================================

def euler(func, y0, a=0., b=10., N=100, plot=True):
    """
    Solve ODE using Euler method over interval [a, b]
    
    Parameters
    ----------
    func : callable
        Function f(t, y) representing dy/dt = f(t, y)
    y0 : float or array
        Initial condition y(a) = y0
    a, b : float
        Time interval [a, b]
    N : int
        Number of steps
    plot : bool, optional
        If True, plot the solution (default: True)
        
    Returns
    -------
    tpoints : ndarray
        Time values
    ypoints : ndarray
        Solution values
        
    Example
    -------
    >>> cooling = lambda t, T: -0.1*(T - 20)
    >>> t, T = euler(cooling, 90.0, a=0, b=60, N=600, plot=False)
    """
    h = (b - a) / N
    tpoints = np.arange(a, b + h, h)  # Include endpoint
    ypoints = np.zeros(len(tpoints))
    
    ypoints[0] = y0
    for i in range(len(tpoints) - 1):
        t = tpoints[i]
        y = ypoints[i]
        ypoints[i+1] = euler_step(y, func, t, h)
    
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(tpoints, ypoints, linewidth=2)
        plt.xlabel("t", fontsize=12)
        plt.ylabel("y(t)", fontsize=12)
        plt.title("Euler Method Solution", fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.show()
    
    return tpoints, ypoints


def rk2(func, y0, a=0., b=10., N=100, plot=True):
    """
    Solve ODE using 2nd order Runge-Kutta (midpoint) method
    
    Parameters
    ----------
    func : callable
        Function f(t, y) representing dy/dt = f(t, y)
    y0 : float or array
        Initial condition y(a) = y0
    a, b : float
        Time interval [a, b]
    N : int
        Number of steps
    plot : bool, optional
        If True, plot the solution (default: True)
        
    Returns
    -------
    tpoints : ndarray
        Time values
    ypoints : ndarray
        Solution values
    """
    h = (b - a) / N
    tpoints = np.arange(a, b + h, h)
    ypoints = np.zeros(len(tpoints))
    
    ypoints[0] = y0
    for i in range(len(tpoints) - 1):
        t = tpoints[i]
        y = ypoints[i]
        ypoints[i+1] = rk2_step(y, func, t, h)
    
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(tpoints, ypoints, linewidth=2)
        plt.xlabel("t", fontsize=12)
        plt.ylabel("y(t)", fontsize=12)
        plt.title("RK2 (Midpoint) Method Solution", fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.show()
    
    return tpoints, ypoints


def rk4(func, y0, a=0., b=10., N=100, plot=True):
    """
    Solve ODE using 4th order Runge-Kutta method
    
    Parameters
    ----------
    func : callable
        Function f(t, y) representing dy/dt = f(t, y)
    y0 : float or array
        Initial condition y(a) = y0
    a, b : float
        Time interval [a, b]
    N : int
        Number of steps
    plot : bool, optional
        If True, plot the solution (default: True)
        
    Returns
    -------
    tpoints : ndarray
        Time values
    ypoints : ndarray
        Solution values
        
    Example
    -------
    >>> cooling = lambda t, T: -0.1*(T - 20)
    >>> t, T = rk4(cooling, 90.0, a=0, b=60, N=60, plot=False)
    """
    h = (b - a) / N
    tpoints = np.arange(a, b + h, h)
    ypoints = np.zeros(len(tpoints))
    
    ypoints[0] = y0
    for i in range(len(tpoints) - 1):
        t = tpoints[i]
        y = ypoints[i]
        ypoints[i+1] = rk4_step(y, func, t, h)
    
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(tpoints, ypoints, linewidth=2)
        plt.xlabel("t", fontsize=12)
        plt.ylabel("y(t)", fontsize=12)
        plt.title("RK4 Method Solution", fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.show()
    
    return tpoints, ypoints


# ============================================================================
# SYSTEM SOLVER FUNCTIONS (for coupled ODEs)
# ============================================================================

def euler_system(func, y0, a=0., b=10., N=100, plot=True):
    """
    Solve system of ODEs using Euler method
    
    Parameters
    ----------
    func : callable
        Function f(t, y) that returns array of derivatives
        y is a 1D array, returns 1D array of same size
    y0 : array_like
        Initial conditions [y1(a), y2(a), ...]
    a, b : float
        Time interval
    N : int
        Number of steps
    plot : bool
        If True, plot all components
        
    Returns
    -------
    tpoints : ndarray
        Time values
    ypoints : ndarray
        Solution values, shape (len(tpoints), len(y0))
    """
    h = (b - a) / N
    tpoints = np.arange(a, b + h, h)
    y0 = np.asarray(y0)
    ypoints = np.zeros((len(tpoints), len(y0)))
    
    ypoints[0] = y0
    for i in range(len(tpoints) - 1):
        t = tpoints[i]
        y = ypoints[i]
        ypoints[i+1] = euler_step(y, func, t, h)
    
    if plot:
        plt.figure(figsize=(10, 6))
        for j in range(len(y0)):
            plt.plot(tpoints, ypoints[:, j], linewidth=2, label=f'y{j+1}')
        plt.xlabel("t", fontsize=12)
        plt.ylabel("y(t)", fontsize=12)
        plt.title("Euler Method - System Solution", fontsize=14)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    return tpoints, ypoints


def rk4_system(func, y0, a=0., b=10., N=100, plot=True):
    """
    Solve system of ODEs using RK4 method
    
    Parameters
    ----------
    func : callable
        Function f(t, y) that returns array of derivatives
    y0 : array_like
        Initial conditions
    a, b : float
        Time interval
    N : int
        Number of steps
    plot : bool
        If True, plot all components
        
    Returns
    -------
    tpoints : ndarray
        Time values
    ypoints : ndarray
        Solution values, shape (len(tpoints), len(y0))
    """
    h = (b - a) / N
    tpoints = np.arange(a, b + h, h)
    y0 = np.asarray(y0)
    ypoints = np.zeros((len(tpoints), len(y0)))
    
    ypoints[0] = y0
    for i in range(len(tpoints) - 1):
        t = tpoints[i]
        y = ypoints[i]
        ypoints[i+1] = rk4_step(y, func, t, h)
    
    if plot:
        plt.figure(figsize=(10, 6))
        for j in range(len(y0)):
            plt.plot(tpoints, ypoints[:, j], linewidth=2, label=f'y{j+1}')
        plt.xlabel("t", fontsize=12)
        plt.ylabel("y(t)", fontsize=12)
        plt.title("RK4 Method - System Solution", fontsize=14)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    return tpoints, ypoints


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Example 1: Newton's Law of Cooling
    print("Example 1: Newton's Law of Cooling")
    print("=" * 50)
    
    def cooling(t, T):
        """dT/dt = -r*(T - T_ambient)"""
        r = 0.1
        T_ambient = 20.0
        return -r * (T - T_ambient)
    
    # Using complete solver
    t1, T1 = rk4(cooling, y0=90.0, a=0, b=60, N=60, plot=False)
    print(f"Final temperature: {T1[-1]:.2f} °C")
    
    # Using manual stepping (same result)
    T = 90.0
    dt = 1.0
    for i in range(60):
        T = rk4_step(T, cooling, i*dt, dt)
    print(f"Manual stepping:   {T:.2f} °C\n")
    
    
    # Example 2: Predator-Prey System
    print("Example 2: Lotka-Volterra Predator-Prey")
    print("=" * 50)
    
    def predator_prey(t, state):
        """
        state = [prey, predators]
        Returns [dprey/dt, dpredators/dt]
        """
        prey, predators = state
        alpha = 1.0    # Prey birth rate
        beta = 0.1     # Predation rate
        gamma = 1.5    # Predator death rate
        delta = 0.075  # Predator reproduction rate
        
        dprey = alpha*prey - beta*prey*predators
        dpredators = delta*prey*predators - gamma*predators
        
        return np.array([dprey, dpredators])
    
    # Initial populations
    initial_state = np.array([40, 9])  # 40 rabbits, 9 foxes
    
    t2, populations = rk4_system(predator_prey, initial_state, 
                                  a=0, b=50, N=500, plot=False)
    print(f"Final populations: {populations[-1, 0]:.1f} prey, {populations[-1, 1]:.1f} predators")