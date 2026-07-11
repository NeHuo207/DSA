def bubble_sort_optimized(a):
    a = a[:]
    n = len(a)
    passes = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        passes += 1
        if not swapped:
            break
    return a, passes


if __name__ == "__main__":
    print(bubble_sort_optimized([1, 2, 3, 4]))
    print(bubble_sort_optimized([2, 3, 1]))
    print(bubble_sort_optimized([5, 4, 3, 2, 1]))
