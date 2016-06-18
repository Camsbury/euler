# -*- coding: utf-8 -*-
"""


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.

"""

def sum_square_difference(num):
    sq_sum = ((num + 1)*num/2)**2
    sum_sq = sum(x**2 for x in range(1,num+1))
    return sq_sum - sum_sq
    
print(sum_square_difference(10))
print(sum_square_difference(100))