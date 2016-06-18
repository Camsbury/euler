# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def n_prime(n):
    count = 1
    current = 3
    while count != n:
        if check_prime(current):
            count += 1
        current += 2
    return current - 2

def check_prime(n):
    for i in range(2,int(n**0.5 + 1)):
        if n%i == 0:
            return False
    return True
    
