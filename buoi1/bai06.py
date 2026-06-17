def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    else:
        return -1


a = [7, 3, 9, 12, 5, 8, 1]
x = int(input("Nhập giá trị cần tìm: "))

kqua = linear_search(a, x)

if kqua != -1:
    print(f"Tìm thấy {x} tại vị trí: {kqua}")
else:
    print(f"Không tìm thấy {x} trong mảng a")