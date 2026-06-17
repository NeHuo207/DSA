def insertion_sort_stable_pairs(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
 
data = [(2, 'a'), (1, 'b'), (2, 'c')]
print("Bài 13:", insertion_sort_stable_pairs(data))  # [(1,'b'),(2,'a'),(2,'c')]