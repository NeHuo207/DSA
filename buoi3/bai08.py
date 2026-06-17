def insertion_s(arr,k):
    for i in range(1,k+1):          # <- Chỉ chạy k vòng thay vì hết cả mảng
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
arr = [4,3,2,1]
k=1
insertion_s(arr,k)
print(arr)