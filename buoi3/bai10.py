def count_inversions_brute(a):
    inv = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inv += 1
    return inv
 
def count_shifts(a):
    b = a[:]
    shifts = 0
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
            shifts += 1
        b[j + 1] = key
    return shifts
 
a = [2, 4, 1, 3]
inv = count_inversions_brute(a)
sh  = count_shifts(a)
print(f"Bài 10: inversions={inv}, shifts={sh}, equal={inv==sh}")  # True