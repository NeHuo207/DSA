def selection_sort_desc(a):
    n = len(a)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a
 
print("Bài 3:", selection_sort_desc([5, 2, 4, 6, 1]))  # [6, 5, 4, 2, 1]