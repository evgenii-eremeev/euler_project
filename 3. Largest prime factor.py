"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from helpers.primes import make_primes

primes = make_primes(10000)
TARGET = 600851475143


def factor(target):
    factors = []
    while target != 1:
        for prime in primes:
            if target % prime == 0:
                factors.append(prime)
                target /= prime
                break
    return factors

# answer
print(max(factor(TARGET)))
