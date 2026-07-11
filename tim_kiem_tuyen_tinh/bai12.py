def max_min(a):
    lon_nhat = a[0]
    vi_tri_lon = 0
    
    nho_nhat = a[0]
    vi_tri_nho = 0


    for i in range(len(a)):
        if a[i] > lon_nhat:
            lon_nhat = a[i]
            vi_tri_lon = i

        if a[i] < nho_nhat:
            nho_nhat = a[i] 
            vi_tri_nho = i

    return lon_nhat, nho_nhat, vi_tri_lon, vi_tri_nho


a = [4, 1, 4, 9, 4]

lon_nhat, nho_nhat, vi_tri_lon, vi_tri_nho = max_min(a)
print(f'Giá trị lớn nhất: {lon_nhat}')
print(f'Vị trí lớn nhất: {vi_tri_lon}')
print(f'Giá trị nhỏ nhất: {nho_nhat}')
print(f'Vị trí nhỏ nhất: {vi_tri_nho}')