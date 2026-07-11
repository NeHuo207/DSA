def magnetic_force(x, m):
    x.sort()
    lo, hi = 1, x[-1] - x[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        count, last = 1, x[0]
        for pos in x[1:]:
            if pos - last >= mid: count += 1; last = pos
        if count >= m: lo = mid
        else:          hi = mid - 1
    return lo   # giống aggressive_cows hoàn toàn!
print(magnetic_force([1,2,3,4,7],3))