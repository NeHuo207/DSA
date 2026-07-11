## Bài 10. Chọn cài đặt theo mật độ đồ thị

- Bản O(V²): tổng chi phí = O(V²).
- Bản heap: tổng chi phí = O((V+E) log V) ≈ O(E log V) khi E ≥ V.

So sánh:
- Nếu **E ≈ V²** (đồ thị dày, gần đầy đủ): O(V²) so với O(V² log V) → bản O(V²) **nhanh hơn** (không có log).
- Nếu **E ≈ V** (đồ thị thưa, ví dụ cây, lưới): O(V²) so với O(V log V) → bản **heap nhanh hơn** rõ rệt.

**Giải thích:** điểm hòa vốn nằm quanh E ≈ V²/log V. Quy tắc thực dụng: đồ thị thưa (E = O(V)) → heap; đồ thị dày (E gần V²) → O(V²) vì tránh overhead của heap.