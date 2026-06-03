def split_array(a, k):
    lo, hi = max(a), sum(a)
    while lo < hi:
        mid = (lo + hi) // 2
        parts, cur = 1, 0
        for x in a:
            if cur + x > mid: parts += 1; cur = 0
            cur += x
        if parts <= k: hi = mid
        else: lo = mid + 1
    return lo
print(split_array( [7,2,5,10,8],2))