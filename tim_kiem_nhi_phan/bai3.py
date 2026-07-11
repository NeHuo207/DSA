def first_pos(a, x):
    lo, hi, res = 0, len(a)-1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            res = mid
            hi = mid - 1   # tiếp tục tìm trái
        elif a[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return res
print(first_pos([1, 2, 2, 2, 3],2))