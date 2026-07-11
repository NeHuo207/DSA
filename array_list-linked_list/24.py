def reverse_inplace(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(f"  [1,2,3,4] -> {reverse_inplace([1, 2, 3, 4])}")
