def insertion_sort(a):
    shift_count = 0
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and key<a[j]:
            a[j+1] = a[j]
            shift_count +=1
            j-=1
        a[j+1] = key
    return a, shift_count
a = [3,2,1]
arr, shifts = insertion_sort(a)
print(arr)
print("Số lần sắp xếp: ", shifts)