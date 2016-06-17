
def main():
    ans = 2
    x = 1
    y = 2
    while y <=4e6:
        sum_temp = x + y
        x = y
        y = sum_temp
        if y%2 == 0:
            ans += y
    return ans