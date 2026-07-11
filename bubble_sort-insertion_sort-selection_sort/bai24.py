import random
def bubble_sort_stats(a):
    b = a[:]; swaps = cmps = 0
    n = len(b)
    for i in range(n):
        for j in range(n - 1 - i):
            cmps += 1
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]; swaps += 1
    return cmps, swaps
 
def selection_sort_stats(a):
    b = a[:]; swaps = cmps = 0
    n = len(b)
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            cmps += 1
            if b[j] < b[mi]: mi = j
        if mi != i:
            b[i], b[mi] = b[mi], b[i]; swaps += 1
    return cmps, swaps
 
def insertion_sort_stats(a):
    b = a[:]; shifts = cmps = 0
    for i in range(1, len(b)):
        key = b[i]; j = i - 1
        while j >= 0:
            cmps += 1
            if b[j] > key:
                b[j + 1] = b[j]; j -= 1; shifts += 1
            else:
                break
        b[j + 1] = key
    return cmps, shifts
 
test = random.sample(range(1, 101), 10)
bc, bs = bubble_sort_stats(test)
sc, ss = selection_sort_stats(test)
ic, ish = insertion_sort_stats(test)
 
print("Bài 24:")
print(f"  {'Algorithm':<18} {'Comparisons':<14} {'Swaps/Shifts'}")
print(f"  {'Bubble Sort':<18} {bc:<14} {bs}")
print(f"  {'Selection Sort':<18} {sc:<14} {ss}")
print(f"  {'Insertion Sort':<18} {ic:<14} {ish}")
# Insertion Sort tốt nhất khi dữ liệu gần sắp xếp