Thuật toán tìm kiếm tuyến tính:

Hoạt động bằng cách duyệt lần lượt từng phần tử trong mảng từ đầu đến cuối để kiểm tra phần tử cần tìm có xuất hiện trong mảng hay không.
Khi duyệt gặp phần từ bằng giá trị cần tìm thì trả về vị trí của phần tử đó.
Khi duyệt hết mảng vẫn không tìm thấy sẽ trả kết luận phần tử không tồn tại trong mảng.
INPUT:

Mảng a = [7, 3, 9, 12, 5]
Giá trị cần tìm x = 12
OUTPUT:

Vị trí của giá trị x trong mảng nếu tìm thấy.
Nếu không tìm thấy sẽ trả về -1
-> Vị trí của giá trị 12 trong mảng nếu tìm thấy là: 3

Thuật toán dừng:

Thuật toán sẽ dừng trong hai trường hợp:
Trường hợp 1: Tìm thấy phần tử.
Trường hợp 2: Duyệt hết mảng nhưng không tìm thấy phần tử.