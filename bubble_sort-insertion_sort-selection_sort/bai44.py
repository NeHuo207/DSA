def double_selection_sort_v2(a):
    n = len(a)
    lo, hi = 0, n - 1
    swaps = 0
    while lo < hi:
        min_idx, max_idx = lo, lo
        for j in range(lo, hi + 1):
            if a[j] < a[min_idx]: min_idx = j
            if a[j] > a[max_idx]: max_idx = j
 
        # Swap min về vị trí lo
        a[lo], a[min_idx] = a[min_idx], a[lo]
        swaps += 1 if lo != min_idx else 0
 
        # Nếu max_idx bị dời khi swap min (max_idx = lo)
        if max_idx == lo:
            max_idx = min_idx
 
        # Swap max về vị trí hi
        a[hi], a[max_idx] = a[max_idx], a[hi]
        swaps += 1 if hi != max_idx else 0
 
        lo += 1; hi -= 1
    return a, swaps
 
arr, sw = double_selection_sort_v2([5, 1, 4, 2, 8, 3])
print(f"Bài 19: {arr}, swaps={sw}")