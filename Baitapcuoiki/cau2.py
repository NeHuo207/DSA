'''
Câu 2 (Thuật toán Sắp xếp)
Cho mảng A = [5, 2, 4, 6, 1, 3]. Hãy tính tổng số lần dịch chuyển (shift) phần tử khi áp dụng thuật toán Insertion Sort để sắp xếp mảng theo thứ tự tăng dần. Đại lượng tính được này có mối liên hệ đặc biệt nào với khái niệm "số nghịch thế" (inversions) của mảng ban đầu?
'''
A = [5,2,4,6,1,3]
def sort(A):
    shiftCount = 0
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            shiftCount += 1
            j -=1
        A[j+1] = key
    return A,shiftCount
print(sort(A))