def bubble_sort_pairs(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort_pairs(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort_pairs(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__":
    data = [(5, "a"), (5, "b"), (3, "c")]
    print(f"ban dau:   {data}")
    print(f"bubble:    {bubble_sort_pairs(data)}")
    print(f"insertion: {insertion_sort_pairs(data)}")
    print(f"selection: {selection_sort_pairs(data)}")
