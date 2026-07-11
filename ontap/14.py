def shell_sort(a, gaps=None):
    a = a[:]
    n = len(a)
    total_shifts = 0

    if gaps is None:
        gaps = []
        gap = n // 2
        while gap > 0:
            gaps.append(gap)
            gap //= 2

    for gap in gaps:
        for i in range(gap, n):
            key = a[i]
            j = i
            while j >= gap and a[j - gap] > key:
                a[j] = a[j - gap]
                j -= gap
                total_shifts += 1
            a[j] = key

    return a, total_shifts


if __name__ == "__main__":
    a = [12, 34, 54, 2, 3, 8, 1, 9]

    r1, s1 = shell_sort(a)
    print(f"gap n/2, n/4...: {r1}  shift={s1}")

    r2, s2 = shell_sort(a, gaps=[4, 2, 1])
    print(f"gap 4,2,1:       {r2}  shift={s2}")

    r3, s3 = shell_sort(a, gaps=[1])
    print(f"gap 1 (insert):  {r3}  shift={s3}")
