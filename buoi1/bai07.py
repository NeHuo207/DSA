def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    else:
        return False


a = [7, 3, 9, 12, 5, 8, 1]
x = int(input("Nhập giá trị cần tìm: "))

kqua = ton_tai(a, x)
print(kqua)