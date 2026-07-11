## Bài 18. Vì sao Dijkstra cần trọng số không âm

Đồ thị: 0→1 (2), 0→2 (5), 2→1 (-4).

Chạy Dijkstra từ 0:
1. Khởi tạo dist=[0, ∞, ∞]. Chốt 0, relax: dist[1]=2, dist[2]=5.
2. Đỉnh có dist nhỏ nhất chưa chốt là 1 (dist=2) → **chốt đỉnh 1 luôn**, coi dist[1]=2 là tối ưu.
3. Sau đó chốt 2 (dist=5), relax cạnh 2→1: 5 + (-4) = 1 < 2, nhưng đỉnh 1 **đã bị chốt** nên Dijkstra bỏ qua, không cập nhật.

→ Kết quả sai: **dist[1] = 2**, trong khi đường thực sự ngắn nhất là 0→2→1 = 5 + (-4) = **1**.

**Giải thích lỗi:** Dijkstra dựa trên giả định "một khi 1 đỉnh có dist nhỏ nhất trong các đỉnh chưa chốt, dist đó không thể bị làm nhỏ hơn nữa qua đỉnh khác" — giả định này chỉ đúng khi mọi trọng số ≥ 0. Cạnh âm phá vỡ nó vì một đường đi qua đỉnh có dist lớn hơn vẫn có thể ngắn hơn về sau.

**Thuật toán thay thế:** dùng **Bellman-Ford** (O(V·E)), thuật toán này relax lặp lại tất cả cạnh V-1 lần và xử lý đúng cả cạnh âm (miễn không có chu trình âm).