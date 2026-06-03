Giả sử mảng có n phần tử.

Thuật toán tìm kiếm tuyến tính sẽ lần lượt so sánh: A[i] == x. Cho đến khi tìm thấy x hoặc duyệt hết mảng.

(a) Trường hợp tốt nhất: - Phần tử x nằm ngay đầu mảng.

Ví dụ: A[0] == x

-> Khi đó chỉ cần 1 phép so sánh. -> Số phép so sánh: 1

(b) Trường hợp xấu nhất: - x nằm ở cuối mảng. - x không có trong mảng.

-> Khi đó thuật toán phải duyệt toàn bộ n phần tử. -> Số phép so sánh: n

(c) Trường hợp trung bình: - Khi phần tử có trong mảng

Giả sử x có khả năng xuất hiện đều ở mọi vị trí.

Nếu x ở vị trí đầu: -> cần 1 phép so sánh
Nếu x ở vị trí thứ 2: -> cần 2 phép so sánh
...
Nếu x ở vị trí thứ n: -> cần n phép so sánh
Số phép so sánh trung bình: tổng: 1 + 2 + 3 + ... + n = n(n + 1) / 2 (đây là công thức tính tổng cấp số cộng)

Tính trung bình: tổng / n = (n(n+1)/2) / n => (n + 1) / 2

Kết luận độ phức tạp thời gian:

Tốt nhất: O(1)

Trung bình: O(n)

Xấu nhất: O(n)

Vì khi n lớn, số phép so sánh tăng tuyến tính theo n nên thuật toán tìm kiếm tuyến tính có độ phức tạp thời gian là: O(n)