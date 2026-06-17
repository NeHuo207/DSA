def insertion_sort_nearly_sorted(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shifts += 1
        a[j + 1] = key
    return a, shifts
 
arr, sh = insertion_sort_nearly_sorted([1, 2, 4, 3, 5])
print(f"Bài 17: {arr}, shifts={sh}")  # shifts=1 → gần O(n)