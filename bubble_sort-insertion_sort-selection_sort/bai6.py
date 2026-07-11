def insertion_sort(a):
    compare_count = 0
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0:
            compare_count+=1
            if key<a[j]:
                a[j+1] = a[j]
                j-=1
            else:
                break
        a[j+1]=key
    return a,compare_count
a = [1,2,3]
arr,compare = insertion_sort(a)
print(arr)
print("Số lần so sánh: ",compare)