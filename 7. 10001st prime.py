"""
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime(num):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


# My first try. SLOW
def find_prime(count):
    primes = [2]
    num = 2
    while len(primes) < count:
        num += 1
        prime_found = True
        for prime in primes:
            if num % prime == 0:
                prime_found = False
        if prime_found:
            primes.append(num)
    return primes


# implemented Sieve of Eratosthenes. Fast. Memory inefficient.
def make_primelist(limit, sieve_len=2000000):
    """
    Returns prime list up to the nth prime.
    Input int > 1
    """
    sieve = [1] * sieve_len
    primes = []
    current_prime = 2
    while len(primes) < limit:
        if sieve[current_prime]:
            primes.append(current_prime)
            for multiple in range(current_prime**2, sieve_len, current_prime):
                sieve[multiple] = 0
        current_prime += 1
    return primes


# answer
print(make_primelist(10001)[-1])






