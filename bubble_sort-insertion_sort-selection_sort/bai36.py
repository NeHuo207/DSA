def selection_sort_pairs(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
 
data = [(2, 'a'), (2, 'b'), (1, 'c')]
result = selection_sort_pairs(data[:])
print(f"Bài 11: {result}")
# (2,'b') có thể đứng trước (2,'a') → không ổn định