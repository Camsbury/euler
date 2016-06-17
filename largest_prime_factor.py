
def largest_prime_factor(dividend):
    for factor in range(2,dividend):
        if dividend%factor == 0:
            if dividend == factor: return factor
            dividend = dividend/factor
        else:
            factor += 1

print(largest_prime_factor(600851475143))