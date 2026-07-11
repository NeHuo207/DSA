def first_occurrence(a, x):
    lo, hi = 0, len(a) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            result = mid
            hi = mid - 1
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def last_occurrence(a, x):
    lo, hi = 0, len(a) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            result = mid
            lo = mid + 1
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def count_occurrences(a, x):
    f = first_occurrence(a, x)
    if f == -1:
        return 0
    return last_occurrence(a, x) - f + 1


if __name__ == "__main__":
    a = [1, 2, 2, 2, 3]
    print(first_occurrence(a, 2))
    print(last_occurrence(a, 2))
    print(count_occurrences(a, 2))
    print(count_occurrences(a, 5))
