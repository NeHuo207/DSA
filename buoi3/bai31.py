def selection_sort_count_cmps(a):
    n = len(a)
    cmps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            cmps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, cmps
 
arr, c = selection_sort_count_cmps([3, 1, 4, 1, 5])
n = len(arr)
print(f"Bài 6: comparisons={c}, n(n-1)/2={n*(n-1)//2}, equal={c == n*(n-1)//2}")