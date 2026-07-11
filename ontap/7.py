def bubble_sort(a):
    a = a[:]
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return a, swaps


def count_inversions_brute(a):
    inv = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inv += 1
    return inv


if __name__ == "__main__":
    a = [2, 3, 1]
    sorted_a, swaps = bubble_sort(a)
    print(sorted_a, swaps)
    print(count_inversions_brute(a))

    b = [5, 4, 3, 2, 1]
    sorted_b, swaps_b = bubble_sort(b)
    print(sorted_b, swaps_b)
    print(count_inversions_brute(b))
