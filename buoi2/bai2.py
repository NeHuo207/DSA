def exists(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if   a[mid] == x: return True
        elif a[mid] < x:  lo = mid + 1
        else: hi = mid - 1
    return False

print(exists([2,4,6,8],5))