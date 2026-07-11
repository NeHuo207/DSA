def ten_sv(ds, x):
    for i in range(len(ds)):
        if ds[i] == x: 
            return i
        
    else: 
        return -1


ds = ["An", "Bình", "Châu"]
x = input('Nhập tên: ').title()

kqua = ten_sv(ds, x)
print(f'vị trí: {kqua}')