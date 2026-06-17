def binary_search(arr,left,right,key):
    if (right >left):
        mid = (left+right)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr,left,mid-1,key)
        else:
            return binary_search(arr,mid+1,right,key)
    else:
        return -1

arr = [2,5,8,12,16,23,38,56,72,91]
key = 5
result = binary_search(arr,0,len(arr)-1,key)
if result != -1:
    print("vi tri tim thay thu i la: ",str(result))
else:
    print("khong tim thay phan tu trong mang")