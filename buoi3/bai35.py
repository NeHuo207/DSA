def selection_sort_exact_swaps(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, swaps
 
arr, sw = selection_sort_exact_swaps([1, 2, 3])
print(f"Bài 10: {arr}, swaps={sw}")  # swaps=0 (đã sắp xếp)