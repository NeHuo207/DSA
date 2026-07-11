def insertion_sort(a):
    a = a[:]
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


def count_inversions_brute(a):
    inv = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inv += 1
    return inv


if __name__ == "__main__":
    a = [3, 2, 1]
    sorted_a, shifts = insertion_sort(a)
    print(sorted_a, shifts)
    print(count_inversions_brute(a))

    b = [4, 3, 2, 10, 12, 1, 5, 6]
    sorted_b, shifts_b = insertion_sort(b)
    print(sorted_b, shifts_b)
    print(count_inversions_brute(b))
