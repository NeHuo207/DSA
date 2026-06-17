Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước.

Giải thích:

Thuật toán này hoạt động bằng cách duyệt lần lượt từng phần tử trong mảng từ đầu đến cuối và so sánh với giá trị x cần tìm.

Do kiểm tra từng phần tử nên dù mảng:

đã sắp xếp
chưa sắp xếp
-> thì thuật toán vẫn hoạt động bình thường.

So sánh với tìm kiếm nhị phân:

Điều kiện áp dụng:
Tìm kiếm tuyến tính: Không cần mảng sắp xếp.

Tìm kiếm nhị phân: Bắt buộc mảng phải được sắp xếp tăng hoặc giảm trước khi tìm.

Độ phức tạp thời gian:
Tìm kiếm tuyến tính: O(n) Trong trường hợp xấu nhất phải duyệt toàn bộ mảng.

Tìm kiếm nhị phân: O(log n) Sau mỗi lần so sánh, phạm vi tìm kiếm giảm còn một nửa nên nhanh hơn nhiều.

Kết luận:

Tìm kiếm tuyến tính: Dễ cài đặt, dùng được cho mọi mảng nhưng chậm hơn.

Tìm kiếm nhị phân: Nhanh hơn nhiều nhưng yêu cầu mảng phải được sắp xếp trước.