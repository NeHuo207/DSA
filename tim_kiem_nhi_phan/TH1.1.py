def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [120, 35, 60, 42, 280, 7, 15, 19]
bubble_sort(arr)
print(arr)
