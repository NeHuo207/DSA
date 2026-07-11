# Giải 25 Bài Tập Thuật Toán Dijkstra

**Đồ thị dùng chung (G1, có hướng, đỉnh 0–5):**
```
adj[0] = [(1,4),(2,1)]
adj[1] = [(3,1)]
adj[2] = [(1,2),(3,5),(4,8)]
adj[3] = [(4,3),(5,6)]
adj[4] = [(5,2)]
adj[5] = []
```

**Đồ thị G2 (vô hướng, thành phố A–E):**
```
A-B: 5, A-C: 3, B-C: 1, B-D: 2, C-D: 6, D-E: 4
```

---

## Bài 1. Biểu diễn đồ thị có trọng số

Không cần Dijkstra, chỉ cần đọc hình vẽ và liệt kê cạnh đi ra từ mỗi đỉnh.

```
FUNCTION build_adj(V, edges):
    adj = mảng V danh sách rỗng
    FOR (u, v, w) IN edges:
        adj[u].append((v, w))     // vì đồ thị có hướng, chỉ thêm 1 chiều
    RETURN adj
```

Kết quả cho G1:
```
adj[0] = [(1,4),(2,1)]
adj[1] = [(3,1)]
adj[2] = [(1,2),(3,5),(4,8)]
adj[3] = [(4,3),(5,6)]
adj[4] = [(5,2)]
adj[5] = []
```

**Giải thích:** danh sách kề là cách biểu diễn đồ thị hiệu quả cho Dijkstra, vì tại mỗi đỉnh ta chỉ cần duyệt các cạnh đi ra từ nó (O(bậc ra)) thay vì cả ma trận.

---

## Bài 2. Tính tay đường đi ngắn nhất (source = 0)

Ý tưởng tính tay: mỗi vòng chọn đỉnh **chưa chốt** có `dist` nhỏ nhất, chốt nó, rồi relax các đỉnh kề.

| Vòng | Đỉnh chọn | dist[0] | dist[1] | dist[2] | dist[3] | dist[4] | dist[5] |
|---|---|---|---|---|---|---|---|
| Khởi tạo | - | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | 0 | 0 | 4 | 1 | ∞ | ∞ | ∞ |
| 2 | 2 (dist=1) | 0 | 3 | 1 | 6 | 9 | ∞ |
| 3 | 1 (dist=3) | 0 | 3 | 1 | 4 | 9 | ∞ |
| 4 | 3 (dist=4) | 0 | 3 | 1 | 4 | 7 | 10 |
| 5 | 4 (dist=7) | 0 | 3 | 1 | 4 | 7 | 9 |
| 6 | 5 (dist=9) | 0 | 3 | 1 | 4 | 7 | 9 |

Thứ tự chốt: **0, 2, 1, 3, 4, 5** — khớp ví dụ đề bài.

**Giải thích:** ở vòng 2, từ đỉnh 0 relax sang 2: dist[2]=1 < ∞. Từ 2 relax sang 1 (0→2→1 = 1+2=3 < 4 cũ) nên cập nhật dist[1]=3. Cứ thế lặp lại: chọn min → chốt → relaxláng giềng.

---

## Bài 3. Dijkstra cơ bản O(V²)

```
FUNCTION dijkstra_v2(adj, n, s):
    dist = mảng n phần tử, tất cả = INF
    dist[s] = 0
    visited = mảng n phần tử, tất cả = false

    REPEAT n LẦN:
        u = -1
        FOR i IN 0..n-1:
            IF NOT visited[i] AND (u == -1 OR dist[i] < dist[u]):
                u = i
        IF dist[u] == INF: BREAK          // phần còn lại không tới được
        visited[u] = true

        FOR (v, w) IN adj[u]:
            IF dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    RETURN dist
```

Kết quả: `dist = [0, 3, 1, 4, 7, 9]` — khớp ví dụ.

**Giải thích:** độ phức tạp O(V²) vì mỗi vòng lặp ngoài (V lần) phải quét tuyến tính để tìm đỉnh chưa chốt có dist nhỏ nhất (O(V)). Phù hợp đồ thị nhỏ/dày.

---

## Bài 4. In khoảng cách tới mọi đỉnh

```
FUNCTION print_distances(dist, n):
    FOR i IN 0..n-1:
        IF dist[i] == INF:
            PRINT i, "-1"
        ELSE:
            PRINT i, dist[i]
```

**Giải thích:** chỉ đơn giản duyệt mảng `dist` đã tính ở Bài 3, quy ước in `-1` (hoặc ∞) cho đỉnh không có đường đi từ nguồn.

---

## Bài 5. Đồ thị vô hướng có trọng số (G2)

```
FUNCTION build_undirected_adj(V, edges):
    adj = mảng V danh sách rỗng
    FOR (u, v, w) IN edges:
        adj[u].append((v, w))
        adj[v].append((u, w))     // thêm cả 2 chiều
    RETURN adj
```

Chạy Dijkstra (giống Bài 3) từ A trên G2:

- A=0
- A→C = 3 → dist[C]=3
- A→C→B = 3+1 = 4 (so với A→B=5) → dist[B]=4
- B→D = 4+2 = 6 → dist[D]=6
- D→E = 6+4 = 10 → dist[E]=10

Kết quả: `A=0, C=3, B=4, D=6, E=10` — khớp ví dụ.

**Giải thích:** với đồ thị vô hướng, mỗi cạnh (u,v,w) được thêm vào danh sách kề của **cả hai** đỉnh; phần lõi thuật toán Dijkstra không đổi.

---

## Bài 6. Đường đi ngắn nhất giữa hai đỉnh (dừng sớm)

```
FUNCTION dijkstra_early_stop(adj, n, s, t):
    dist = mảng n phần tử = INF; dist[s] = 0
    pq = priority_queue chứa (0, s)     // (khoảng cách, đỉnh)
    visited = mảng n phần tử = false

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()
        IF visited[u]: CONTINUE
        visited[u] = true
        IF u == t: RETURN d              // dừng sớm ngay khi lấy t ra

        FOR (v, w) IN adj[u]:
            IF dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.push((dist[v], v))

    RETURN dist[t]   // nếu vòng lặp kết thúc mà chưa gặp t
```

Với s=0, t=4: kết quả = **7** (đường 0→2→1→3→4).

**Giải thích:** vì Dijkstra chốt đỉnh theo thứ tự dist tăng dần, một khi `t` được lấy ra khỏi hàng đợi ưu tiên (tức được chốt), dist[t] chắc chắn là tối ưu — không cần chạy tiếp tới hết đồ thị.

---

## Bài 7. Truy vết đường đi (parent[])

```
FUNCTION dijkstra_with_parent(adj, n, s):
    dist = mảng n = INF; dist[s] = 0
    parent = mảng n = -1
    pq = priority_queue chứa (0, s)
    visited = mảng n = false

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()
        IF visited[u]: CONTINUE
        visited[u] = true
        FOR (v, w) IN adj[u]:
            IF dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                pq.push((dist[v], v))
    RETURN dist, parent

FUNCTION reconstruct_path(parent, s, t):
    path = []
    cur = t
    WHILE cur != -1:
        path.append(cur)
        IF cur == s: BREAK
        cur = parent[cur]
    REVERSE(path)
    RETURN path
```

Với s=0, t=4: `parent = [-1, 2, 0, 1, 3, ...]` → truy ngược: 4 → 3 → 1 → 2 → 0 → đảo lại: **0 → 2 → 1 → 3 → 4** (độ dài 7).

**Giải thích:** mỗi lần relax cạnh (u→v) thành công, ta ghi `parent[v] = u`. Sau khi thuật toán chạy xong, truy ngược từ `t` theo `parent` tới `s` rồi đảo chiều mảng sẽ cho đường đi.

---

## Bài 8. Số đỉnh trong bán kính D

```
FUNCTION count_within_radius(dist, n, D):
    count = 0
    FOR i IN 0..n-1:
        IF dist[i] <= D:
            count += 1
    RETURN count
```

Với D=3 trên G1 (dist = [0,3,1,4,7,9]): đỉnh 0(0), 2(1), 1(3) thỏa ≤3 → **3 đỉnh**.

**Giải thích:** chạy Dijkstra một lần lấy mảng `dist[]`, sau đó chỉ cần đếm phần tử ≤ D — bài toán phụ đơn giản dựa trên kết quả Bài 3.

---

## Bài 9. Dijkstra với hàng đợi ưu tiên (heap)

```
FUNCTION dijkstra_heap(adj, n, s):
    dist = mảng n = INF; dist[s] = 0
    pq = min_heap chứa (0, s)
    visited = mảng n = false

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()          // O(log V)
        IF visited[u]: CONTINUE
        visited[u] = true

        FOR (v, w) IN adj[u]:          // tổng cộng O(E) lần trên toàn thuật toán
            IF dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.push((dist[v], v))  // O(log V)

    RETURN dist
```

**Giải thích:** mỗi cạnh chỉ gây tối đa 1 lần push vào heap → tổng số thao tác heap là O(E), mỗi thao tác O(log V) → độ phức tạp **O((V+E) log V)**. Với n, m tới 10^5–2×10^5 thì bản O(V²) (≈10^10 phép tính) sẽ quá chậm, bắt buộc phải dùng heap.

---

## Bài 10. Chọn cài đặt theo mật độ đồ thị

- Bản O(V²): tổng chi phí = O(V²).
- Bản heap: tổng chi phí = O((V+E) log V) ≈ O(E log V) khi E ≥ V.

So sánh:
- Nếu **E ≈ V²** (đồ thị dày, gần đầy đủ): O(V²) so với O(V² log V) → bản O(V²) **nhanh hơn** (không có log).
- Nếu **E ≈ V** (đồ thị thưa, ví dụ cây, lưới): O(V²) so với O(V log V) → bản **heap nhanh hơn** rõ rệt.

**Giải thích:** điểm hòa vốn nằm quanh E ≈ V²/log V. Quy tắc thực dụng: đồ thị thưa (E = O(V)) → heap; đồ thị dày (E gần V²) → O(V²) vì tránh overhead của heap.

---

## Bài 11. Nhiều nguồn (multi-source)

```
FUNCTION multi_source_dijkstra(adj, n, sources):
    dist = mảng n = INF
    pq = min_heap rỗng
    FOR s IN sources:
        dist[s] = 0
        pq.push((0, s))
    visited = mảng n = false

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()
        IF visited[u]: CONTINUE
        visited[u] = true
        FOR (v, w) IN adj[u]:
            IF dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.push((dist[v], v))

    RETURN dist   // dist[i] = khoảng cách tới nguồn gần nhất
```

**Giải thích:** thay vì tạo "siêu nguồn" ảo nối tới mọi nguồn với trọng số 0 (cách làm bằng lý thuyết đồ thị), ta có thể mô phỏng trực tiếp bằng cách **khởi tạo heap với tất cả nguồn cùng dist=0** — hai cách tương đương về kết quả. Với nguồn={0,3}: dist[i] = min(dist theo 0, dist theo 3).

---

## Bài 12. Đi qua đỉnh bắt buộc

```
FUNCTION shortest_via_k(adj, adj_reverse, n, s, t, k):
    dist_from_s = dijkstra(adj, n, s)            // Bài 3/9
    dist_from_k = dijkstra(adj, n, k)             // từ k đi xuôi tới t
    dist_to_k   = dijkstra(adj_reverse, n, k)      // từ k lùi để lấy dist(s,k) nếu đồ thị có hướng

    // nếu đồ thị vô hướng: dist(s,k) = dist(k,s) nên chỉ cần 1 lần chạy từ k
    result = dist_to_k[s] + dist_from_k[t]
    RETURN result
```

Với s=0, t=5, qua k=2: dist(0,2) = 1, dist(2,5) = min(2→1→3→5, 2→3→5, 2→4→5) = 1+2+1+6=10 hoặc 2→3→5=5+6=11, 2→4→5=8+2=10... chọn nhỏ nhất → cộng dồn ra kết quả.

**Giải thích:** vì Dijkstra chỉ tìm đường ngắn nhất giữa 1 cặp/1 nguồn, để bắt buộc đi qua k, ta tách bài toán thành 2 nửa độc lập: s→k và k→t, rồi cộng lại. Đây là kỹ thuật rất phổ biến (cũng áp dụng được cho "đi qua cạnh bắt buộc").

---

## Bài 13. Đếm số đường đi ngắn nhất

```
FUNCTION count_shortest_paths(adj, n, s):
    dist = mảng n = INF; dist[s] = 0
    ways = mảng n = 0; ways[s] = 1
    pq = min_heap chứa (0, s)
    visited = mảng n = false

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()
        IF visited[u]: CONTINUE
        visited[u] = true
        FOR (v, w) IN adj[u]:
            IF dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                ways[v] = ways[u]              // tìm ra đường ngắn hơn hẳn -> reset số cách
                pq.push((dist[v], v))
            ELSE IF dist[u] + w == dist[v]:
                ways[v] += ways[u]             // tìm thêm 1 đường ngắn nhất khác cùng độ dài
    RETURN ways
```

**Giải thích:** thêm mảng `ways[]`. Khi relax tìm ra đường **ngắn hơn**, số cách được ghi đè bằng số cách tới u. Khi tìm ra đường có độ dài **bằng** đường ngắn nhất hiện tại, cộng dồn số cách. Ví dụ trong đề: 2 đường cùng dài 7 tới t → ways[t] = 2.

---

## Bài 14. Đường đi ngắn nhì

```
FUNCTION second_shortest(adj, n, s):
    dist1 = mảng n = INF     // ngắn nhất
    dist2 = mảng n = INF     // ngắn nhì
    pq = min_heap chứa (0, s)

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()
        IF d > dist2[u]: CONTINUE      // không còn giá trị, bỏ qua

        FOR (v, w) IN adj[u]:
            nd = d + w
            IF nd < dist1[v]:
                dist2[v] = dist1[v]     // dist1 cũ trở thành dist2 mới
                dist1[v] = nd
                pq.push((nd, v))
            ELSE IF dist1[v] < nd < dist2[v]:
                dist2[v] = nd
                pq.push((nd, v))
    RETURN dist1, dist2
```

**Giải thích:** không đánh dấu `visited` như Dijkstra thường, vì một đỉnh có thể được lấy ra khỏi hàng đợi **2 lần** — lần 1 ứng với đường ngắn nhất, lần 2 ứng với đường ngắn nhì. Với mỗi đỉnh ta giữ 2 giá trị dist tốt nhất (cho phép dùng lại cạnh/đỉnh).

---

## Bài 15. Dijkstra trên lưới (grid)

Lưới chi phí:
```
1 3 1
1 5 1
4 2 1
```

```
FUNCTION grid_dijkstra(cost, R, C):
    dist = ma trận R x C = INF
    dist[0][0] = cost[0][0]
    pq = min_heap chứa (dist[0][0], 0, 0)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    WHILE pq KHÔNG RỖNG:
        (d, r, c) = pq.pop_min()
        IF d > dist[r][c]: CONTINUE
        FOR (dr, dc) IN directions:
            nr, nc = r+dr, c+dc
            IF (nr, nc) HỢP LỆ trong lưới:
                nd = d + cost[nr][nc]
                IF nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    pq.push((nd, nr, nc))
    RETURN dist[R-1][C-1]
```

Tính tay: S=(0,0) chi phí vào ô là 1.
Đường 1→1→5→1→1 hoặc đi vòng dưới: 1→1→4→2→1 = 9; đường trên+phải: 1→3→1→1→1=7... So sánh các đường:
- Xuống-xuống-phải-phải: (0,0)=1,(1,0)=1,(2,0)=4,(2,1)=2,(2,2)=1 → tổng = 1+1+4+2+1 = 9
- Phải-phải-xuống-xuống: (0,0)=1,(0,1)=3,(0,2)=1,(1,2)=1,(2,2)=1 → tổng = 1+3+1+1+1 = 7
- **Nhỏ nhất = 7**

**Giải thích:** mỗi ô trong lưới coi như 1 đỉnh, có cạnh 2 chiều nối tới tối đa 4 ô lân cận với trọng số = chi phí bước **vào** ô đích. Bản chất vẫn là Dijkstra chuẩn, chỉ khác cách sinh danh sách kề (sinh động, theo tọa độ thay vì mảng adj cố định).

---

## Bài 16. Trọng số trên đỉnh

```
FUNCTION transform_vertex_weighted(adj, n, cost):
    // Tách mỗi đỉnh v thành v_in và v_out
    // cạnh nội bộ: v_in -> v_out với trọng số cost[v]
    new_adj = đồ thị mới với 2n đỉnh
    FOR v IN 0..n-1:
        new_adj[v_in].add(v_out, cost[v])
    FOR (u, v, w) IN adj:
        new_adj[u_out].add(v_in, w)     // giữ nguyên trọng số cạnh gốc (0 nếu chỉ có trọng số đỉnh)
    RETURN new_adj

// Sau đó chạy Dijkstra bình thường từ s_out tới t_in (hoặc t_out nếu muốn tính luôn chi phí đỉnh t)
```

**Giải thích:** Dijkstra chuẩn chỉ làm việc với trọng số trên cạnh. Để xử lý chi phí đặt trên đỉnh, ta "bổ đôi" mỗi đỉnh v thành v_in (cổng vào) và v_out (cổng ra), nối chúng bằng 1 cạnh có trọng số = c[v]. Mọi cạnh gốc (u→v) được nối lại thành u_out → v_in. Từ đó bài toán trở về dạng trọng số-trên-cạnh quen thuộc.

---

## Bài 17. Đường đi bottleneck (minimax)

```
FUNCTION minimax_path(adj, n, s):
    dist = mảng n = INF        // dist[v] = cạnh lớn nhất nhỏ nhất trên đường tới v
    dist[s] = 0
    pq = min_heap chứa (0, s)
    visited = mảng n = false

    WHILE pq KHÔNG RỖNG:
        (d, u) = pq.pop_min()
        IF visited[u]: CONTINUE
        visited[u] = true
        FOR (v, w) IN adj[u]:
            nd = MAX(dist[u], w)          // phép "relax" đổi thành lấy max cạnh trên đường
            IF nd < dist[v]:
                dist[v] = nd
                pq.push((nd, v))
    RETURN dist
```

**Giải thích:** thay vì cộng dồn trọng số, ta theo dõi "cạnh lớn nhất đã đi qua" trên mỗi đường. Phép relax đổi từ `dist[u]+w` thành `max(dist[u], w)`, và ta vẫn chọn đường có giá trị này **nhỏ nhất**. Tính chất tham lam của Dijkstra (chốt đỉnh có giá trị nhỏ nhất) vẫn đúng vì hàm max cũng đơn điệu không giảm dọc đường đi.

---

## Bài 18. Vì sao Dijkstra cần trọng số không âm

Đồ thị: 0→1 (2), 0→2 (5), 2→1 (-4).

Chạy Dijkstra từ 0:
1. Khởi tạo dist=[0, ∞, ∞]. Chốt 0, relax: dist[1]=2, dist[2]=5.
2. Đỉnh có dist nhỏ nhất chưa chốt là 1 (dist=2) → **chốt đỉnh 1 luôn**, coi dist[1]=2 là tối ưu.
3. Sau đó chốt 2 (dist=5), relax cạnh 2→1: 5 + (-4) = 1 < 2, nhưng đỉnh 1 **đã bị chốt** nên Dijkstra bỏ qua, không cập nhật.

→ Kết quả sai: **dist[1] = 2**, trong khi đường thực sự ngắn nhất là 0→2→1 = 5 + (-4) = **1**.

**Giải thích lỗi:** Dijkstra dựa trên giả định "một khi 1 đỉnh có dist nhỏ nhất trong các đỉnh chưa chốt, dist đó không thể bị làm nhỏ hơn nữa qua đỉnh khác" — giả định này chỉ đúng khi mọi trọng số ≥ 0. Cạnh âm phá vỡ nó vì một đường đi qua đỉnh có dist lớn hơn vẫn có thể ngắn hơn về sau.

**Thuật toán thay thế:** dùng **Bellman-Ford** (O(V·E)), thuật toán này relax lặp lại tất cả cạnh V-1 lần và xử lý đúng cả cạnh âm (miễn không có chu trình âm).

---

## Bài 19. Đường đi xác suất lớn nhất

```
FUNCTION max_probability_path(adj, n, s, t):
    // adj[u] = danh sách (v, p) với p là xác suất thành công cạnh u->v
    prob = mảng n = 0
    prob[s] = 1
    pq = max_heap chứa (1, s)     // lấy ra xác suất lớn nhất trước
    visited = mảng n = false

    WHILE pq KHÔNG RỖNG:
        (p, u) = pq.pop_max()
        IF visited[u]: CONTINUE
        visited[u] = true
        IF u == t: RETURN p

        FOR (v, edge_p) IN adj[u]:
            np = p * edge_p
            IF np > prob[v]:
                prob[v] = np
                pq.push((np, v))
    RETURN prob[t]
```

**Giải thích:** hai cách quy về Dijkstra:
1. **Đổi phép relax:** thay `dist[u]+w` bằng `prob[u]*edge_p`, và dùng **max-heap** thay vì min-heap (tối đa hoá thay vì tối thiểu hoá).
2. **Dùng -log:** vì xác suất ∈ (0,1], `-log(p)` luôn dương, và `-log(p1*p2) = -log(p1) + (-log(p2))`. Đặt trọng số cạnh = `-log(edge_p)`, bài toán trở thành Dijkstra cộng trọng số chuẩn (tìm tổng nhỏ nhất), sau đó lấy `exp(-tổng)` để ra xác suất lớn nhất.

---

## Bài 20. K đường đi ngắn nhất

```
FUNCTION k_shortest_paths(adj, n, s, t, K):
    count = mảng n = 0             // số lần đỉnh được lấy ra khỏi heap
    result = []                     // các độ dài đường đi ngắn nhất tìm được, theo thứ tự tăng
    pq = min_heap chứa (0, s)

    WHILE pq KHÔNG RỖNG AND LEN(result) < K:
        (d, u) = pq.pop_min()
        IF count[u] >= K: CONTINUE      // đỉnh u đã được dùng đủ K lần, bỏ qua
        count[u] += 1
        IF u == t:
            result.append(d)
        FOR (v, w) IN adj[u]:
            pq.push((d + w, v))          // không cần kiểm tra visited, cho phép lặp đỉnh

    RETURN result
```

Với K=3, s=0,t=5: `result = [7, 9, 10]` — khớp ví dụ.

**Giải thích:** khác Dijkstra chuẩn (chỉ chốt mỗi đỉnh 1 lần), ở đây mỗi đỉnh được phép "lấy ra" tối đa K lần khỏi heap. Mỗi lần lấy `u` ra là ứng với 1 đường đi (không nhất thiết đơn giản, có thể lặp đỉnh) tới `u` theo thứ tự độ dài tăng dần. Khi `u == t` đủ K lần, ta có K đường đi ngắn nhất tới t.

---

## Bài 21. Dijkstra trên trạng thái mở rộng

```
FUNCTION dijkstra_extended_state(s, target, max_fuel):
    // trạng thái = (đỉnh, nhiên_liệu_còn_lại)
    dist = dictionary, mặc định INF
    dist[(s, max_fuel)] = 0
    pq = min_heap chứa (0, s, max_fuel)

    WHILE pq KHÔNG RỖNG:
        (d, u, fuel) = pq.pop_min()
        IF d > dist[(u, fuel)]: CONTINUE
        IF u == target: RETURN d

        FOR (v, w, fuel_cost) IN adj[u]:
            new_fuel = fuel - fuel_cost
            IF new_fuel >= 0:
                nd = d + w
                state = (v, new_fuel)
                IF nd < dist.get(state, INF):
                    dist[state] = nd
                    pq.push((nd, v, new_fuel))
        // (nếu có trạm tiếp nhiên liệu tại đỉnh, thêm bước "refuel" thành 1 cạnh đặc biệt)

    RETURN INF   // không tới được
```

**Giải thích:** khi đường đi ngắn nhất còn phụ thuộc thông tin phụ (nhiên liệu, vé miễn phí, thời gian...), ta **mở rộng không gian trạng thái**: đỉnh của đồ thị mới là cặp `(đỉnh gốc, thông tin phụ)` thay vì chỉ đỉnh gốc. Dijkstra chạy y hệt trên đồ thị trạng thái này — chỉ số lượng đỉnh tăng lên (nhân với số giá trị có thể của thông tin phụ).

---

## Bài 22. Giới hạn số cạnh trung chuyển (tối đa k cạnh)

```
FUNCTION shortest_at_most_k_edges(adj, n, s, t, k):
    // trạng thái = (đỉnh, số_cạnh_đã_dùng)
    dist = ma trận (n) x (k+1) = INF
    dist[s][0] = 0
    pq = min_heap chứa (0, s, 0)

    WHILE pq KHÔNG RỖNG:
        (d, u, edges_used) = pq.pop_min()
        IF d > dist[u][edges_used]: CONTINUE
        IF edges_used == k: CONTINUE       // hết lượt, không đi tiếp

        FOR (v, w) IN adj[u]:
            nd = d + w
            IF nd < dist[v][edges_used + 1]:
                dist[v][edges_used + 1] = nd
                pq.push((nd, v, edges_used + 1))

    RETURN MIN(dist[t][0..k])
```

Với k=1 (tối đa 1 điểm dừng = tối đa 2 cạnh): kết quả ≤ 2 cạnh, khớp ví dụ.

**Giải thích:** đây cũng là một dạng "trạng thái mở rộng" (giống Bài 21), với thông tin phụ là số cạnh đã dùng. Vì Dijkstra bình thường không quan tâm số bước, ta cần thêm chiều `edges_used` vào trạng thái để giới hạn đúng k cạnh; đáp án cuối là min trên mọi số cạnh từ 0 đến k.

---

## Bài 23. Nhiều truy vấn đường đi ngắn nhất

```
// Chiến lược A: chạy Dijkstra riêng cho mỗi truy vấn (s, t)
FOR each query (s, t):
    RUN dijkstra_early_stop(adj, n, s, t)     // Bài 6
// Tổng chi phí: O(Q * (V+E) log V)

// Chiến lược B: tiền xử lý — chạy Dijkstra từ mỗi đỉnh nguồn xuất hiện trong các truy vấn
distinct_sources = tập hợp các s xuất hiện trong query
precomputed = {}
FOR s IN distinct_sources:
    precomputed[s] = dijkstra_heap(adj, n, s)     // Bài 9
FOR each query (s, t):
    answer = precomputed[s][t]
// Tổng chi phí: O(|distinct_sources| * (V+E) log V), truy vấn sau đó O(1)
```

**Giải thích đánh đổi:**
- Nếu số truy vấn Q **nhỏ** hoặc nguồn luôn khác nhau → chiến lược A đơn giản, không tốn bộ nhớ phụ.
- Nếu Q **lớn** nhưng số nguồn **phân biệt** ít (nhiều truy vấn dùng chung nguồn) → chiến lược B (tiền xử lý + cache) hiệu quả hơn nhiều, đổi bộ nhớ O(V × |distinct_sources|) lấy tốc độ truy vấn O(1).
- Nếu mọi cặp (s,t) đều có thể được hỏi và V nhỏ → có thể tiền xử lý **Floyd-Warshall** O(V³) một lần cho all-pairs.

---

## Bài 24. Dijkstra vs Bellman-Ford vs A*

| Tiêu chí | Dijkstra | Bellman-Ford | A* |
|---|---|---|---|
| Cạnh âm | Không hỗ trợ (sai, xem Bài 18) | Hỗ trợ (miễn không có chu trình âm) | Không hỗ trợ (thường dùng như Dijkstra có định hướng) |
| Độ phức tạp | O(V²) hoặc O((V+E) log V) | O(V·E) | Giống Dijkstra nhưng thực tế duyệt ít đỉnh hơn nếu heuristic tốt |
| Đặc điểm | Tham lam, chốt đỉnh dist nhỏ nhất | Relax tất cả cạnh V-1 lần, phát hiện chu trình âm | Dùng heuristic h(v) ước lượng khoảng cách còn lại tới đích để ưu tiên duyệt |

```
FUNCTION a_star(adj, n, s, t, heuristic):
    dist = mảng n = INF; dist[s] = 0
    pq = min_heap chứa (heuristic(s), s)       // ưu tiên theo f(v) = dist[v] + h(v)
    visited = mảng n = false
    visited_count = 0

    WHILE pq KHÔNG RỖNG:
        (f, u) = pq.pop_min()
        IF visited[u]: CONTINUE
        visited[u] = true
        visited_count += 1
        IF u == t: RETURN dist[t], visited_count

        FOR (v, w) IN adj[u]:
            nd = dist[u] + w
            IF nd < dist[v]:
                dist[v] = nd
                pq.push((nd + heuristic(v), v))

    RETURN INF, visited_count
```

**Giải thích:** A* giống Dijkstra nhưng sắp xếp hàng đợi theo `f(v) = dist[v] + h(v)` thay vì chỉ `dist[v]`, với `h(v)` là hàm heuristic ước lượng (ví dụ khoảng cách Manhattan/Euclid trên lưới) khoảng cách còn lại tới đích. Nếu `h` là **admissible** (không bao giờ ước lượng quá khoảng cách thực), A* vẫn đảm bảo tìm ra đường ngắn nhất nhưng thường duyệt ít đỉnh hơn Dijkstra vì được "định hướng" về phía đích.

---

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

---

*Ghi chú:* các bài dùng heap (9, 13, 14, 17, 19, 20, 21, 22, 24) đều có thể triển khai bằng `heapq` (Python), `priority_queue` (C++), hoặc `PriorityQueue` (Java). Nếu cần code thật (Python/C++) cho bài cụ thể nào, nói mình làm tiếp nhé.