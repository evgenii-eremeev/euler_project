"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""



def sum_of_primes(limit):
    """
    Returns prime list up to the limit.
    Input int > 1
    """
    sieve = [1] * limit # make a list where index == number. 1 - prime, 0 - not prime.
    primes = []
    current_prime = 2
    while current_prime < limit:
        if sieve[current_prime]:
            primes.append(current_prime)
            # when new prime is fount we should check all multiples of that prime as non-primes.
            # we start loop at current_prime**2 becouse we alredy checked all non-primes before.
            for multiple in xrange(current_prime**2, limit, current_prime):
                sieve[multiple] = 0
        current_prime += 1
    return sum(primes)

print sum_of_primes(2000000)