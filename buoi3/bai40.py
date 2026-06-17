def partial_selection_sort(a, k):
    n = len(a)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
 
arr = partial_selection_sort([5, 3, 1, 4, 2], 2)
print(f"Bài 15: {arr}")  # [1, 2, ...] (2 phần tử đầu đúng vị trí)