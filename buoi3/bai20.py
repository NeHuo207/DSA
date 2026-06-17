def shell_sort(a, use_knuth=True):
    n = len(a)
    # Tạo dãy gap (Knuth: 1, 4, 13, 40,...)
    if use_knuth:
        gap = 1
        gaps = []
        while gap < n:
            gaps.append(gap)
            gap = gap * 3 + 1
        gaps = list(reversed(gaps))
    else:
        gaps = []
        g = n // 2
        while g > 0:
            gaps.append(g)
            g //= 2
 
    shifts = 0
    for gap in gaps:
        for i in range(gap, n):
            key = a[i]
            j = i - gap
            while j >= 0 and a[j] > key:
                a[j + gap] = a[j]
                j -= gap
                shifts += 1
            a[j + gap] = key
    return a, shifts
 
arr, sh = shell_sort([8, 7, 6, 5, 4, 3, 2, 1])
print(f"Bài 20: {arr}, shifts={sh}")
 