# works in python 2

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import urllib2

url = "https://primes.utm.edu/lists/small/10000.txt"
primes = urllib2.urlopen(url).read()
primes = map(int, primes[167:primes.find('end')].split())

TARGET = 600851475143

def factor(target):
    factors = []
    while target != 1:
        for prime in primes:
            if target % prime == 0:
                factors.append(prime)
                target /= prime
                print prime
                break
        print 'for-loop ended', factors
    return factors

#answer
print max(factor(TARGET))