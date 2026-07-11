def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    a = [1, 3, 5, 7]
    print(lower_bound(a, 4))
    print(upper_bound(a, 4))

    b = [1, 2, 2, 2, 3]
    print(lower_bound(b, 2))
    print(upper_bound(b, 2))
