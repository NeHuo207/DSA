def binary_insertion_sort(a):
    cmp_normal = 0
    cmp_binary = 0
 
    # Đếm so sánh bản thường
    b = a[:]
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0:
            cmp_normal += 1
            if b[j] > key:
                b[j + 1] = b[j]
                j -= 1
            else:
                break
        b[j + 1] = key
 
    # Binary insertion sort
    c = a[:]
    for i in range(1, len(c)):
        key = c[i]
        lo, hi = 0, i
        while lo < hi:
            mid = (lo + hi) // 2
            cmp_binary += 1
            if c[mid] <= key:
                lo = mid + 1
            else:
                hi = mid
        for j in range(i, lo, -1):
            c[j] = c[j - 1]
        c[lo] = key
 
    return c, cmp_normal, cmp_binary
 
arr, cn, cb = binary_insertion_sort([5, 2, 4, 6, 1, 3])
print(f"Bài 9: {arr}, normal_cmps={cn}, binary_cmps={cb}")