import numpy as np
from scipy.optimize import root_scalar
from fractions import Fraction

# Define the function here
def func(x):
    return np.sin(2*x) - np.sqrt(3)/2 # This is your function

# Define the ranges
x_ranges = [(0, np.pi/2), (np.pi/2, np.pi), (np.pi, 3*np.pi/2), (3*np.pi/2, 2*np.pi)]

# Solve the equation within each range
for x_range in x_ranges:
    try:
        solution = root_scalar(func, method='brentq', bracket=x_range)

        if solution.converged:
            # Convert the solution to a fraction in terms of π
            frac = Fraction(solution.root/np.pi).limit_denominator()
            solution_str = f"{frac.numerator if frac.numerator != 1 else ''}π/{frac.denominator if frac.denominator != 1 else ''}"
            print(f"The solution is {solution_str}")
    except ValueError:
        continue
