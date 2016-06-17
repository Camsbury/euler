
def largest_palindrome_product():
    for pal_half in range(997,99,-1):
        pal = int(str(pal_half) + str(pal_half)[::-1])
        for div in range(999,99,-1):
            if pal/div >= 1000:
                break
            if pal%div == 0:
                return pal

print(largest_palindrome_product())