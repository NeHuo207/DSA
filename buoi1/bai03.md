A = [7, 3, 9, 12, 5, 8, 1]

(a) x = 7

B.1: i = 0 B.2: A[0] = 7 == x

Output: Tìm thấy x tại vị trí i = 0. Số phép so sánh: 1

(b) x = 1

B.1: i = 0 B.2: A[0] = 7 != x

B.1: i = 1 B.2: A[1] = 3 != x

B.1: i = 2 B.2: A[2] = 9 != x

B.1: i = 3 B.2: A[3] = 12 != x

B.1: i = 4 B.2: A[4] = 5 != x

B.1: i = 5 B.2: A[5] = 8 != x

B.1: i = 6 B.2: A[6] = 1 == x

Output: Tìm thấy x tại vị trí i = 6. Số phép so sánh: 7

(c) x = 100

B.1: i = 0 B.2: A[0] = 7 != x

B.1: i = 1 B.2: A[1] = 3 != x

B.1: i = 2 B.2: A[2] = 9 != x

B.1: i = 3 B.2: A[3] = 12 != x

B.1: i = 4 B.2: A[4] = 5 != x

B.1: i = 5 B.2: A[5] = 8 != x

B.1: i = 6 B.2: A[6] = 1 != x

Output: Không tìm thấy x trong mảng. Số phép so sánh: 7

Nhận xét:

Nếu giá trị x cần tìm nằm gần đầu mảng thì số phép so sánh càng ít
Nếu giá trị x cần tìm nằm gần cuối mảng thì số phép so sánh càng nhiều
Nếu giá tri x không tồn tại trong mảng thì thuật toán phải duyệt toàn bộ mảng.