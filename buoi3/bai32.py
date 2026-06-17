def selection_sort_chars(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
 
print("Bài 7:", selection_sort_chars(['d', 'a', 'c', 'b']))  # ['a','b','c','d']