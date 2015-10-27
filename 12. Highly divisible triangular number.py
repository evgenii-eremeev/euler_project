"""
https://projecteuler.net/problem=12
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
from collections import Counter
from functools import reduce
from helpers.primes import primes_below

prime_list = primes_below(65501)


def nth_triangle(n):
    return (n + 1) * n // 2


def count_divs_old(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


def count_divs(num):
    if num == 1 or num == 0:
        return num
    prime_divisors = []
    idx = 0
    divided_num = num
    while divided_num != 1:
        if divided_num % prime_list[idx] == 0:
            prime_divisors.append(prime_list[idx])
            divided_num //= prime_list[idx]
        else:
            idx += 1
    prime_counter = Counter(prime_divisors)
    #     Any integer N can be expressed as follows:
    # N = p1**a1 * p2**a2 * p3**a3 * ...
    # where p1, p2, p3... is a distinct prime number, and a1, a2, a3... is its exponent.
    # For example, 28 = 2**2 * 7**2
    # Furthermore, the number of divisors D(N) of any integer N can be computed from:
    # D(N) = (a1+1)*(a2+1)*(a3+1)*(...)
    # a1, a2, a3... being the exponents of the distinct prime numbers which are factors of N
    values_plus_one = map(lambda a: a + 1, prime_counter.values())
    all_divisors = reduce(lambda x, y: x * y, values_plus_one)
    return all_divisors



def triangle_num_with_divs_over(limit):
    divs = 0
    n = 1
    while divs < limit:
        triangle_value = nth_triangle(n)
        divs = count_divs(triangle_value)
        n += 1
    return triangle_value

# answer
print(triangle_num_with_divs_over(500))
