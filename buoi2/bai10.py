def search_rotated(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x: return mid
        if a[lo] <= a[mid]:          
            if a[lo] <= x < a[mid]: hi = mid - 1
            else: lo = mid + 1
        else:                        
            if a[mid] < x <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
print(search_rotated([4, 5, 6, 7, 0, 1, 2],0))