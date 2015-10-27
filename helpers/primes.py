def make_primes(limit, sieve_len=2000000):
    """
    Returns prime list up to the limit.
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


def primes_below(sieve_len):
    """
    Returns list of primes below input number
    """
    sieve = [1] * sieve_len
    primes = []
    current_prime = 2
    while current_prime < sieve_len:
        if sieve[current_prime]:
            primes.append(current_prime)
            for multiple in range(current_prime**2, sieve_len, current_prime):
                sieve[multiple] = 0
        current_prime += 1
    return primes
