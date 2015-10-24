"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import urllib2
import math
import mytime

url = "https://primes.py.utm.edu/lists/small/10000.txt"
primes = urllib2.urlopen(url).read()
primes = map(int, primes[167:primes.find('end')].split())


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

# answer
# print find_prime(10001)[-1]


# solution by forum member
def find_nth_prime(n):
    seive = [0]*2000000

    current_prime = 2
    current_prime_index = 1

    while 1<2:
        if current_prime_index == n:
            break


        #we set all the multiples of the current prime to 1	
        for value in xrange(current_prime,len(seive), current_prime):
            seive[value] = 1

        #we find the next prime
        for index in xrange(current_prime+1,len(seive)):
            if seive[index] == 0:
                current_prime = index
                current_prime_index += 1
                break

    return current_prime



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
            for multiple in xrange(current_prime**2, sieve_len, current_prime):
                sieve[multiple] = 0
        current_prime += 1
    return primes

#print "My first try:", mytime.mytime(find_prime, 10001) #SLOW!
#print "By someone:", mytime.mytime(find_nth_prime, 10001)
#print "My best shot:", mytime.mytime(make_primelist, 10001)

#print make_primelist(10000) == primes.py





