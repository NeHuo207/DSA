"""
BÀI 25 — Bài chứng minh (không cần code)
 
BẤT BIẾN VÒNG LẶP (Loop Invariant):
    Trước mỗi lần lặp ngoài thứ i (i từ 1 đến n-1):
    Đoạn a[0..i-1] chứa đúng i phần tử ban đầu của a[0..i-1]
    và chúng đã được sắp xếp theo thứ tự tăng dần.
 
CHỨNG MINH 3 BƯỚC:
 
1. KHỞI TẠO (Initialization):
   Trước vòng lặp đầu tiên (i = 1):
   a[0..0] gồm 1 phần tử → hiển nhiên đã sắp xếp. 
 
2. DUY TRÌ (Maintenance):
   Giả sử bất biến đúng trước vòng lặp thứ i.
   Khi đó a[0..i-1] đã sắp. Vòng trong tìm vị trí j thỏa
   a[j] ≤ key < a[j+1], dịch a[j+1..i-1] sang phải một ô,
   rồi đặt key vào a[j+1].
   Kết quả: a[0..i] chứa đúng các phần tử ban đầu của a[0..i]
   và đã sắp xếp → bất biến đúng trước vòng i+1. 
 
3. KẾT THÚC (Termination):
   Vòng ngoài kết thúc khi i = n.
   Bất biến ⟹ a[0..n-1] đã sắp xếp đúng.
   Vòng ngoài lặp n-1 lần → thuật toán luôn dừng. 
 
KẾT LUẬN: Insertion Sort đúng đắn và luôn dừng. □
"""