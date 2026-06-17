def insertion_sort_abs(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and abs(a[j]) > abs(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
 
print("Bài 11:", insertion_sort_abs([-3, 1, -2, 2]))  # [1, -2, 2, -3]