def dem_xuat_hien(a, x):
    dem = 0
    for i in range(len(a)):
        if a[i] == x:
            dem += 1

    return dem


a = [2, 5, 2, 7, 2]
x = 2

dem = dem_xuat_hien(a, x)
print(f"Kết quả xuất hiện: {dem}")