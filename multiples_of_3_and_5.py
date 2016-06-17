def sum_below_1000():
    sum_3 = sum(x for x in range(0,1000,3))
    sum_5 = sum(x for x in range(0,1000,5))
    sum_15 = sum(x for x in range(0,1000,15))
    return sum_3 + sum_5 - sum_15