def double_selection_sort(a):
    cmps_single = cmps_double = 0
    n = len(a)
 
    # Bản thường
    b = a[:]
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            cmps_single += 1
            if b[j] < b[mi]: mi = j
        b[i], b[mi] = b[mi], b[i]
 
    # Double selection
    c = a[:]
    lo, hi = 0, n - 1
    while lo < hi:
        min_idx, max_idx = lo, lo
        for j in range(lo, hi + 1):
            cmps_double += 1
            if c[j] < c[min_idx]: min_idx = j
            if c[j] > c[max_idx]: max_idx = j
        c[lo], c[min_idx] = c[min_idx], c[lo]
        # Nếu max_idx trùng vị trí lo (đã bị swap), cập nhật
        if max_idx == lo:
            max_idx = min_idx
        c[hi], c[max_idx] = c[max_idx], c[hi]
        lo += 1; hi -= 1
 
    return c, cmps_single, cmps_double
 
arr, cs, cd = double_selection_sort([5, 1, 4, 2, 8])
print(f"Bài 9: {arr}, single_cmps={cs}, double_cmps={cd}")