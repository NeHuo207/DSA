# Tính tay đường đi ngắn nhất
**Vòng lặp 0**
Vòng: 0
Đỉnh: chưa có
Cập nhập: Khởi tạo
dist[] sau khi cập nhập: [0, ∞, ∞, ∞, ∞, ∞]
**Vòng lặp 1**
Vòng: 1
Đỉnh: 0
Cập nhập: 0 → 1 = 4, 0 → 2= 1
dist[] sau khi cập nhập: [0, 4, 1, ∞, ∞, ∞]
**Vòng lặp 2**
Vòng: 2
Đỉnh: 2
Cập nhập: 2 → 1 = 2+1= 3, 2 → 3 =1+5= 6, 2 → 4 =1+8= 9
dist[] sau khi cập nhập: [0, 3, 1, 6, 9, ∞]
**Vòng lặp 3**
Vòng: 3
Đỉnh: 1
Cập nhập: 1 → 3 = 1+2+1 = 4
dist[] sau khi cập nhập: [0, 3, 1, 4, 9, ∞]
**Vòng lặp 4**
Vòng: 4
Đỉnh: 3
Cập nhập: 3 → 4 =1+2+1+3= 7, 3 → 5 =1+2+1+6= 10
dist[] sau khi cập nhập: [0, 3, 1, 4, 7, 10]
**Vòng lặp 5**
Vòng: 5
Đỉnh: 4
Cập nhập: 4 → 5 =1+2+1+3+2= 9
dist[] sau khi cập nhập: [0, 3, 1, 4, 7, 9]
**Vòng lặp 6**
Vòng: 6
Đỉnh: 5
Cập nhập: Không cập nhập
dist[] sau khi cập nhập: [0, 3, 1, 4, 7, 9]
**Kết Luận**
0 → 2 → 1 → 3 → 4 → 5
Với: 
     dist[0] = 0
     dist[1] = 3
     dist[2] = 1
     dist[3] = 4
     dist[4] = 7
     dist[5] = 9
**Đường đi ngắn nhất từ điểm 0 có độ dài**
[0, 3, 1, 4, 7, 9]