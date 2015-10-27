"""
https://projecteuler.net/problem=15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

import math

fact = math.factorial

# answer based on binomial coefficient formula
print(fact(40) / (fact(20) * fact(40 - 20)))
