def lower_bound(a, lo, hi, x):
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_insertion_sort(a):
    a = a[:]
    comparisons = 0
    shifts = 0

    for i in range(1, len(a)):
        key = a[i]
        pos = lower_bound(a, 0, i, key)

        cnt = 0
        n = i
        while n > 0:
            n //= 2
            cnt += 1
        comparisons += cnt

        j = i
        while j > pos:
            a[j] = a[j - 1]
            j -= 1
            shifts += 1
        a[pos] = key

    return a, comparisons, shifts


def insertion_sort(a):
    a = a[:]
    comparisons = 0
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            j -= 1
            shifts += 1
        if j >= 0:
            comparisons += 1
        a[j + 1] = key
    return a, comparisons, shifts


if __name__ == "__main__":
    a = [5, 2, 4, 6, 1, 3]

    r1, c1, s1 = insertion_sort(a)
    print(f"insertion:        {r1}  so_sanh={c1}  shift={s1}")

    r2, c2, s2 = binary_insertion_sort(a)
    print(f"binary insertion: {r2}  so_sanh={c2}  shift={s2}")
