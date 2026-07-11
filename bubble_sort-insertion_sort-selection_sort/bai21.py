def count_inversions(a):
    if len(a) <= 1:
        return a[:], 0
    mid = len(a) // 2
    left, li = count_inversions(a[:mid])
    right, ri = count_inversions(a[mid:])
    merged = []
    inv = li + ri
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, inv
 
import random
big = random.sample(range(100000), 1000)
_, total_shifts = count_inversions(big)
print(f"Bài 21: Tổng shift (n=1000) = {total_shifts}")