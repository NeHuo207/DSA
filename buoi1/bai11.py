def gia_tri_lon_nhat(a):
    lon_nhat = a[0]
    vi_tri = 0
    for i in range(len(a)):
        if a[i] > lon_nhat:
            lon_nhat = a[i]
            vi_tri = i

    return lon_nhat, vi_tri


a = [4, 1, 4, 9, 4]

lon_nhat, vi_tri = gia_tri_lon_nhat(a)
print(f"Giá trị lớn nhất: {lon_nhat}")
print(f"Vị trí: {vi_tri}")