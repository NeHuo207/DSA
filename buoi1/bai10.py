def hien_cuoi_cung(a, x):
    ds =[]
    for i in range(len(a)):
        if a[i] == x:
            ds.append(i)

    if len(a) == 0: 
        return -1

    ds.sort(reverse=True)
    return ds[0]


a = [4, 1, 4, 9, 4]
x = 4

ds = hien_cuoi_cung(a, x)
print(ds)