def selection_sort(a):
    a = a[:]
    n = len(a)
    comparisons = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a, comparisons


if __name__ == "__main__":
    for arr in [[5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [3, 1, 4, 5, 2]]:
        result, comps = selection_sort(arr)
        n = len(arr)
        print(f"{arr} -> {result}  so_sanh={comps}  n(n-1)/2={n*(n-1)//2}")
