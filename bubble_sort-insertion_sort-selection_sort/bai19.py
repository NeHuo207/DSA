def gnome_sort(a):
    ops = 0
    i = 0
    while i < len(a):
        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            ops += 1
            i -= 1
    return a, ops
 
arr, ops = gnome_sort([3, 2, 1])
print(f"Bài 19: {arr}, swaps={ops}")  # [1, 2, 3]