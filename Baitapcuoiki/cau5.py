'''
Câu 5 (Ứng dụng Hàng đợi - Queue)
Cho mảng A = [4, 2, 12, 11, -5, 8, 1, 5, 6] và kích thước cửa sổ trượt k = 3. Thay vì tìm giá trị lớn nhất, hãy mô tả quá trình sử dụng cấu trúc Deque (Hàng đợi hai đầu) để tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt. Trình bày trạng thái của Deque ở 3 bước dịch chuyển đầu tiên và đưa ra mảng kết quả.
'''
from collections import deque

def min_sliding_window(A, k):
    dq = deque()  # lưu index, giá trị tăng dần từ front đến back
    result = []

    for i in range(len(A)):
        # loại index ra khỏi cửa sổ
        if dq and dq[0] <= i - k:
            dq.popleft()

        # loại các phần tử >= A[i] ở cuối
        while dq and A[dq[-1]] >= A[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(A[dq[0]])

    return result

A5 = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
print(min_sliding_window(A5,k))