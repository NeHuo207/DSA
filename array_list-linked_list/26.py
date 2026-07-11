def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return arr


print(f"  [1,2,3,4,5], k=2 -> {rotate_right([1, 2, 3, 4, 5], 2)}")
