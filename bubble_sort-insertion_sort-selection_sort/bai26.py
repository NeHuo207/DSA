def move_min_to_front(a):
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    a[0], a[min_idx] = a[min_idx], a[0]
    return a
 
print("Bài 1:", move_min_to_front([4, 2, 7, 1, 3]))  # [1, 2, 7, 4, 3]