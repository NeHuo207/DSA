def ship_capacity(w, D):
    lo, hi = max(w), sum(w)    # [max_w .. tổng_w]
    while lo < hi:
        mid = (lo + hi) // 2
        days, cur = 1, 0
        for wi in w:
            if cur + wi > mid: days += 1; cur = 0
            cur += wi
        if days <= D: hi = mid
        else: lo = mid + 1
    return lo
print(ship_capacity([1,2,3,4,5,6,7,8,9,10],5))