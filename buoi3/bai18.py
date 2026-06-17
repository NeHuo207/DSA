def is_right_to_left(a):
    cmps = 0
    b = a[:]
    for i in range(1, len(b)):
        key = b[i]; j = i - 1
        while j >= 0:
            cmps += 1
            if b[j] > key:
                b[j + 1] = b[j]; j -= 1
            else:
                break
        b[j + 1] = key
    return b, cmps
 
def is_left_to_right(a):
    cmps = 0
    b = a[:]
    for i in range(1, len(b)):
        key = b[i]
        pos = 0
        while pos < i:
            cmps += 1
            if b[pos] > key:
                break
            pos += 1
        for j in range(i, pos, -1):
            b[j] = b[j - 1]
        b[pos] = key
    return b, cmps
 
a = [1, 2, 4, 3, 5]
_, cr = is_right_to_left(a)
_, cl = is_left_to_right(a)
print(f"Bài 18: right_to_left_cmps={cr}, left_to_right_cmps={cl}")
# Dò phải→trái dừng sớm khi gần sắp xếp → ít so sánh hơn