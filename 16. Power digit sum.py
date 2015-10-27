"""
https://projecteuler.net/problem=16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
from functools import reduce

power = str(2**1000)
sum_digits = reduce(lambda a, b: int(a) + int(b), power)

# answer
print(sum_digits)
