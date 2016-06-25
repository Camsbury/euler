# -*- coding: utf-8 -*-
"""
Find the pythagorean triple a^2 + b^2 = c^2 where a+b+c = 1000
"""

def find_triple(k):
    k = float(k)
    a = 1.
    b = (k**2. - 2.*k*a)/(2.*k-2.*a)
    while not b.is_integer():
        a += 1
        b = (k**2. - 2.*k*a)/(2.*k-2.*a)
    c = (a**2.+b**2.)**0.5
    return a*b*c