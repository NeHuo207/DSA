def insertion_sort(a,x):
    a.append(x)
    key = a[-1]
    j = len(a)-2
    while j>=0 and key<a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
a = [1,3,5,7]
x = 4
insertion_sort(a,x)
print(a)