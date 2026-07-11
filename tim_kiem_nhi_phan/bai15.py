def k_closest(a, k, x):
    lo, hi = 0, len(a) - k
    while lo < hi:
        mid = (lo + hi) // 2
        # So sánh khoảng cách từ x đến a[mid] và a[mid+k]
        if x - a[mid] > a[mid+k] - x: lo = mid + 1
        else: hi = mid
    return a[lo : lo+k]
print(k_closest([1,2,3,4,5],4,3))