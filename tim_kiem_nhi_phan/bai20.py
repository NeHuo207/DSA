def book_alloc(p, m):
    lo, hi = max(p), sum(p)
    while lo < hi:
        mid = (lo + hi) // 2
        students, cur = 1, 0
        for pages in p:
            if cur + pages > mid: students += 1; cur = 0
            cur += pages
        if students <= m: hi = mid
        else: lo = mid + 1
    return lo
print(book_alloc([12,34,67,90],2))