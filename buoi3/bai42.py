def kth_smallest(a, k):
    b = a[:]
    n = len(b)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if b[j] < b[min_idx]:
                min_idx = j
        b[i], b[min_idx] = b[min_idx], b[i]
    return b[k - 1]
 
print(f"Bài 17: {kth_smallest([7, 2, 5, 1, 9], 3)}")  # 5