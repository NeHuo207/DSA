def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    a = [1, 3, 5, 7, 9]
    print(binary_search(a, 7))
    print(binary_search(a, 1))
    print(binary_search(a, 4))
