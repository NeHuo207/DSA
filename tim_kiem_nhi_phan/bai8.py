def isqrt(n):
    if n == 0: return 0
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi + 1) // 2  # làm tròn lên tránh vòng lặp vô tận
        if mid * mid <= n: lo = mid
        else: hi = mid - 1
    return lo

print(isqrt(8))