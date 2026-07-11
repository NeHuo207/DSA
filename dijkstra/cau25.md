## Bài 25. Chứng minh tính đúng đắn của Dijkstra

**Bất biến tham lam (invariant):** Tại thời điểm một đỉnh `u` được lấy ra khỏi hàng đợi ưu tiên (tức "chốt"), giá trị `dist[u]` đang giữ chính là khoảng cách ngắn nhất thực sự từ `s` tới `u`.

**Chứng minh (quy nạp theo thứ tự chốt):**

- *Cơ sở:* đỉnh đầu tiên được chốt là `s` với `dist[s]=0`, hiển nhiên tối ưu.
- *Giả sử đúng cho k đỉnh đã chốt trước đó.* Xét đỉnh `u` sắp được chốt tiếp theo, với `dist[u]` là giá trị nhỏ nhất trong các đỉnh chưa chốt.
- Giả sử có đường đi khác `P` từ `s` tới `u` thực sự ngắn hơn `dist[u]`. Đường `P` phải đi qua ít nhất 1 đỉnh **chưa chốt** trước khi tới `u` (vì nếu toàn bộ đường P chỉ gồm đỉnh đã chốt, theo giả thiết quy nạp `dist[u]` qua đường đó đã được cập nhật đúng và tối ưu rồi, mâu thuẫn với giả sử "còn đường ngắn hơn").
- Gọi `x` là đỉnh chưa chốt đầu tiên trên `P`. Vì **mọi trọng số ≥ 0**, đoạn đường từ `s` tới `x` trong `P` có độ dài ≤ độ dài toàn bộ `P` < `dist[u]`.
- Nhưng `dist[x]` (đã được relax đúng vì đỉnh trước `x` trên `P` đã chốt) ≤ đoạn đường đó < `dist[u]`.
- Điều này mâu thuẫn với việc `u` được chọn là đỉnh có `dist` nhỏ nhất trong các đỉnh chưa chốt (vì `x` cũng chưa chốt mà `dist[x] < dist[u]`).
- Vậy giả sử sai → không tồn tại đường ngắn hơn → `dist[u]` là tối ưu. ∎

**Vì sao cần trọng số không âm:** bước mấu chốt "đoạn đường từ s tới x ≤ toàn bộ đường P" chỉ đúng nếu các cạnh còn lại từ x tới u (phần sau của P) có tổng trọng số ≥ 0. Nếu có cạnh âm, phần đường đi qua đỉnh đã chốt vẫn có thể "được cứu" bởi 1 đoạn cực âm phía sau, khiến 1 đường đi qua đỉnh dist lớn hơn vẫn ngắn hơn — đúng như tình huống sai ở Bài 18.