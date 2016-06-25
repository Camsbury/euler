# -*- coding: utf-8 -*-
"""
sum all primes below 2 million
"""

def sum_primes(k):
    primes = [2]
    check = 3
    while check < k:
        for prime in primes:
            if prime > (check**0.5 + 1):
                primes.append(check)
                break
            if check % prime == 0:
                break
        else:
            primes.append(check)
        check += 2
    return reduce(lambda x,y: x+y, primes)