def remove_if(arr, condition):
    write = 0
    for read in range(len(arr)):
        if not condition(arr[read]):
            arr[write] = arr[read]
            write += 1
    del arr[write:]
    return arr
print(f"  [1,2,3,4] xóa chẵn -> {remove_if([1, 2, 3, 4], lambda v: v % 2 == 0)}")