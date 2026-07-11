def find_min_index(a, i):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx
 
a = [9, 3, 7, 1, 5]
print(f"Bài 8: min index from i=1 → {find_min_index(a, 1)}")  # 3