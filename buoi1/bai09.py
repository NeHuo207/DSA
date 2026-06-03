def tim_tat_ca(a, x):
    ds = []
    for i in range(len(a)):
        if a[i] == x:
            ds.append(i)

    return ds


a = [4, 1, 4, 9, 4]
x = 4

ds = tim_tat_ca(a, x)
print(ds)