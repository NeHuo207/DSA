import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if is_prime(a[i]):
            return a[i], i
    return -1