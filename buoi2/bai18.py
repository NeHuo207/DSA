def kth_missing(a, k):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] - (mid+1) < k: lo = mid + 1
        else: hi = mid
    return lo + k
print(kth_missing([2,3,4,7,11],5))