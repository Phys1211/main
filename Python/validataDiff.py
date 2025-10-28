import numpy as np
from mydiff import forward, backward, central

# Test with a simple function where we know the exact derivative
# f(x) = x^2, so f'(x) = 2x

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = x**2  # y = [0, 1, 4, 9, 16, 25]

print("Testing with f(x) = x^2, so f'(x) = 2x")
print("="*60)
print(f"x values: {x}")
print(f"y values: {y}")
print()

# Compute derivatives
dy_forward, x_forward = forward(y, x)
dy_backward, x_backward = backward(y, x)
dy_central, x_central = central(y, x)

print("Forward Difference:")
print(f"  x positions:  {x_forward}")
print(f"  dy/dx:        {dy_forward}")
print(f"  Expected 2x:  {2*x_forward}")
print(f"  Errors:       {dy_forward - 2*x_forward}")
print()

print("Backward Difference:")
print(f"  x positions:  {x_backward}")
print(f"  dy/dx:        {dy_backward}")
print(f"  Expected 2x:  {2*x_backward}")
print(f"  Errors:       {dy_backward - 2*x_backward}")
print()

print("Central Difference:")
print(f"  x positions:  {x_central}")
print(f"  dy/dx:        {dy_central}")
print(f"  Expected 2x:  {2*x_central}")
print(f"  Errors:       {dy_central - 2*x_central}")
print()

# Manual calculation to verify backward is correct
print("Manual verification of backward difference:")
print("At x=1: [y(1) - y(0)] / [1 - 0] = [1 - 0] / 1 = 1.0")
print(f"        Backward function gives: {dy_backward[0]}")
print("At x=2: [y(2) - y(1)] / [2 - 1] = [4 - 1] / 1 = 3.0")
print(f"        Backward function gives: {dy_backward[1]}")
print("At x=3: [y(3) - y(2)] / [3 - 2] = [9 - 4] / 1 = 5.0")
print(f"        Backward function gives: {dy_backward[2]}")
