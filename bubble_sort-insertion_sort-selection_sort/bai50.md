"""
BÀI 25 — Bài chứng minh (không cần code)
 
BẤT BIẾN VÒNG LẶP (Loop Invariant):
    Sau khi hoàn thành vòng lặp ngoài thứ i (i từ 0 đến n-2):
    a[0..i] chứa đúng (i+1) phần tử NHỎ NHẤT của mảng ban đầu
    và chúng đã được sắp xếp theo thứ tự tăng dần.
 
CHỨNG MINH 3 BƯỚC:
 
1. KHỞI TẠO (Initialization):
   Trước vòng lặp đầu tiên (i = 0):
   a[0..-1] là đoạn rỗng → bất biến đúng hiển nhiên. ✓
 
2. DUY TRÌ (Maintenance):
   Giả sử sau vòng i-1: a[0..i-1] chứa i phần tử nhỏ nhất đã sắp.
   Vòng lặp i tìm min_idx = chỉ số của phần tử nhỏ nhất trong a[i..n-1].
   → a[min_idx] là phần tử nhỏ nhất trong phần chưa sắp xếp,
     và lớn hơn hoặc bằng a[i-1] (vì a[0..i-1] chứa i phần tử nhỏ nhất).
   Sau khi swap(a[i], a[min_idx]):
     a[0..i] chứa (i+1) phần tử nhỏ nhất, sắp tăng dần. ✓
 
3. KẾT THÚC (Termination):
   Vòng ngoài kết thúc khi i = n-1.
   Bất biến ⟹ a[0..n-2] chứa (n-1) phần tử nhỏ nhất đã sắp.
   Phần tử còn lại a[n-1] là lớn nhất → cả mảng đã sắp. ✓
   Vòng ngoài lặp n-1 lần → thuật toán luôn dừng. ✓
 
KẾT LUẬN: Selection Sort đúng đắn và luôn dừng. □
"""