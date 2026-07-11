def bubble_sort_count_swaps(a):
    b = a[:]
    swaps = 0
    n = len(b)
    for i in range(n):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                swaps += 1
    return swaps
 
def selection_sort_count_swaps2(a):
    b = a[:]
    swaps = 0
    n = len(b)
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            if b[j] < b[mi]: mi = j
        if mi != i:
            b[i], b[mi] = b[mi], b[i]
            swaps += 1
    return swaps
 
test = [5, 3, 1, 4, 2]
ss = selection_sort_count_swaps2(test)
bs = bubble_sort_count_swaps(test)
print(f"Bài 18: selection_swaps={ss} (≤n-1), bubble_swaps={bs} (= số nghịch thế)")
# Selection luôn ≤ n-1; bubble = số nghịch thế (có thể lớn hơn nhiều)