def aggressive_cows(x, c):
    x.sort()
    lo, hi = 1, x[-1] - x[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2  
        count, last = 1, x[0]
        for pos in x[1:]:
            if pos - last >= mid: count += 1; last = pos
        if count >= c: lo = mid
        else: hi = mid - 1
    return lo
print(aggressive_cows([1,2,4,8,9],3))