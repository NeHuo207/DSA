def first_pos(a, x):
    lo, hi, res = 0, len(a)-1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            res = mid
            hi = mid - 1   # tiếp tục tìm trái
        elif a[mid] < x: lo = mid + 1
        else:            hi = mid - 1
    return res

def last_pos(a, x):
    lo, hi, res = 0, len(a)-1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            res = mid
            lo = mid + 1   # tiếp tục tìm phải
        elif a[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return res

def count_occur(a, x):
    first = first_pos(a, x)
    if first == -1: return 0
    last  = last_pos(a, x)
    return last - first + 1

print(count_occur([1, 2, 2, 2, 3],2))