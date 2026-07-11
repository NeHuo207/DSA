## PHẦN A — BẢNG BĂM

### Bài 1. Bảng băm bằng chaining
```
CLASS HashTableChaining:
    buckets = mảng m danh sách liên kết rỗng

    FUNCTION hash(key): RETURN hash_code(key) MOD m

    FUNCTION put(key, value):
        idx = hash(key)
        FOR (k, v) IN buckets[idx]:
            IF k == key: cập nhật v = value; RETURN
        buckets[idx].append((key, value))

    FUNCTION get(key):
        idx = hash(key)
        FOR (k, v) IN buckets[idx]:
            IF k == key: RETURN v
        RETURN NOT_FOUND

    FUNCTION remove(key):
        idx = hash(key)
        XÓA cặp (key, _) khỏi buckets[idx] nếu có
```

### Bài 2. Bảng băm bằng dò tuyến tính (linear probing)
```
CLASS HashTableOpenAddressing:
    table = mảng m phần tử = EMPTY

    FUNCTION hash(key): RETURN hash_code(key) MOD m

    FUNCTION put(key, value):
        idx = hash(key)
        WHILE table[idx] != EMPTY AND table[idx].key != key:
            idx = (idx + 1) MOD m         // dò ô kế tiếp
        table[idx] = (key, value)

    FUNCTION get(key):
        idx = hash(key)
        start = idx
        WHILE table[idx] != EMPTY:
            IF table[idx].key == key: RETURN table[idx].value
            idx = (idx + 1) MOD m
            IF idx == start: BREAK
        RETURN NOT_FOUND
```

### Bài 3. Đếm tần suất
```
FUNCTION count_frequency(arr):
    freq = {}
    FOR x IN arr:
        freq[x] = freq.get(x, 0) + 1
    RETURN freq
```

### Bài 4. Hai mảng có phần tử chung
```
FUNCTION common_elements(a, b):
    set_a = SET(a)
    result = set()
    FOR x IN b:
        IF x IN set_a: result.add(x)
    RETURN result
```

### Bài 5. Nhóm theo khóa (group by)
```
FUNCTION group_by(words, key_func):
    groups = {}
    FOR w IN words:
        k = key_func(w)
        IF k NOT IN groups: groups[k] = []
        groups[k].append(w)
    RETURN groups
```

### Bài 6. So sánh chaining vs open addressing
```
// Chaining: mỗi bucket là 1 danh sách; bộ nhớ phụ trội (con trỏ) nhưng chịu được load factor > 1;
//   xóa đơn giản (xóa nút khỏi danh sách).
// Open addressing: mọi phần tử nằm trực tiếp trong mảng, tiết kiệm bộ nhớ hơn khi load thấp,
//   nhưng khi load factor cao dễ bị "clustering" làm chậm; xóa phức tạp (cần lazy deletion, Bài 14).
```

### Bài 7. Hệ số tải và rehashing
```
FUNCTION put_with_rehash(table, key, value):
    IF (table.n + 1) / table.m > 0.75:
        rehash(table)
    table.insert(key, value)
    table.n += 1

FUNCTION rehash(table):
    old_entries = ALL cặp (key, value) trong table
    table.m = table.m * 2
    table.buckets = mảng mới kích thước table.m, rỗng
    FOR (key, value) IN old_entries:
        table.insert(key, value)     // băm lại theo m mới
```

### Bài 8. Quadratic probing / double hashing
```
// Quadratic probing:
FUNCTION probe_quadratic(key, i):
    RETURN (hash(key) + i*i) MOD m

// Double hashing:
FUNCTION probe_double(key, i):
    RETURN (hash1(key) + i * hash2(key)) MOD m
```

### Bài 9. Two Sum dùng hash
```
FUNCTION two_sum(a, target):
    seen = {}                    // value -> index
    FOR i IN 0..LEN(a)-1:
        complement = target - a[i]
        IF complement IN seen:
            RETURN (seen[complement], i)
        seen[a[i]] = i
    RETURN NOT_FOUND
```

### Bài 10. Phần tử không lặp đầu tiên
```
FUNCTION first_unique(s):
    freq = count_frequency(s)
    FOR ch IN s:
        IF freq[ch] == 1: RETURN ch
    RETURN NOT_FOUND
```

### Bài 11. Cài đặt HashSet
```
CLASS HashSet:
    table = HashTableChaining()

    FUNCTION add(x): table.put(x, true)
    FUNCTION contains(x): RETURN table.get(x) != NOT_FOUND
    FUNCTION remove(x): table.remove(x)
```

### Bài 12. Tổng đoạn con bằng k
```
FUNCTION count_subarrays_sum_k(a, k):
    prefix_count = {0: 1}
    prefix_sum = 0, count = 0
    FOR x IN a:
        prefix_sum += x
        IF (prefix_sum - k) IN prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    RETURN count
```

### Bài 13. Dãy liên tiếp dài nhất
```
FUNCTION longest_consecutive(a):
    num_set = SET(a)
    best = 0
    FOR x IN num_set:
        IF (x - 1) NOT IN num_set:      // x là điểm bắt đầu 1 dãy
            length = 1
            WHILE (x + length) IN num_set:
                length += 1
            best = MAX(best, length)
    RETURN best
```

### Bài 14. Xóa lười trong open addressing
```
FUNCTION remove_lazy(table, key):
    idx = hash(key)
    WHILE table[idx] != EMPTY:
        IF table[idx] != DELETED AND table[idx].key == key:
            table[idx] = DELETED       // đánh dấu tombstone, không để trống hẳn
            RETURN true
        idx = (idx + 1) MOD m
    RETURN false

// Khi tìm kiếm (get), tiếp tục dò qua cả ô DELETED (không dừng ở đó)
// Định kỳ dọn dẹp: build lại bảng bỏ hết các ô DELETED khi số tombstone quá nhiều
```

### Bài 15. Băm nhất quán (Consistent Hashing)
```
CLASS ConsistentHashRing:
    ring = cây/mảng có thứ tự các điểm trên vòng băm (0..2^32-1)
    servers = {}                       // vị trí trên vòng -> server

    FUNCTION add_server(server, num_virtual_nodes):
        FOR i IN 0..num_virtual_nodes-1:
            pos = hash(server + "#" + i)
            ring.insert(pos)
            servers[pos] = server

    FUNCTION get_server(key):
        pos = hash(key)
        target = điểm đầu tiên trên ring >= pos (đi vòng nếu cần)
        RETURN servers[target]
// Khi thêm/bớt 1 server, chỉ các khóa nằm giữa server đó và server liền trước bị ảnh hưởng
// → trung bình chỉ ~1/n khóa cần di chuyển
```

## PHẦN B — HÀM BĂM

### Bài 1. Hàm băm modulo cho số nguyên
```
FUNCTION hash_modulo(k, m):
    RETURN k MOD m
```

### Bài 2. Hàm băm cho chuỗi (tổng mã ký tự)
```
FUNCTION hash_sum(s, m):
    total = 0
    FOR ch IN s:
        total += ASCII(ch)
    RETURN total MOD m
// Nhược điểm: các hoán vị ký tự (vd "abc" và "cba") cho cùng 1 giá trị hash
```

### Bài 3. Hàm băm đa thức (polynomial rolling hash)
```
FUNCTION polynomial_hash(s, p, m):
    h = 0
    FOR i IN 0..LEN(s)-1:
        h = (h * p + ASCII(s[i])) MOD m
    RETURN h
// p là cơ số (thường là số nguyên tố nhỏ, vd 31), m là modulo lớn (nguyên tố) để giảm va chạm
```

### Bài 4. Đếm va chạm của một hàm băm
```
FUNCTION count_collisions(keys, hash_func, m):
    buckets = {}
    FOR k IN keys:
        idx = hash_func(k) MOD m
        buckets[idx] = buckets.get(idx, 0) + 1
    collisions = SUM(count - 1 FOR count IN buckets.values() IF count > 1)
    RETURN collisions
```

### Bài 5. Vì sao chọn m là số nguyên tố
```
// Thực nghiệm: so sánh phân bố khi m = 16 (2^4) và m = 17 (nguyên tố)
FUNCTION compare_distribution(keys, m1, m2):
    dist1 = phân bố bucket khi hash keys với m1
    dist2 = phân bố bucket khi hash keys với m2
    IN RA độ lệch chuẩn của dist1 và dist2 để so sánh độ đều
// Giải thích: nếu m = 2^k, hash chỉ phụ thuộc vào các bit thấp của khóa → dễ dồn cụm
// nếu khóa có pattern theo bit. Số nguyên tố tránh được các ước số chung với khóa.
```

### Bài 6. Rolling hash & Rabin–Karp
```
FUNCTION rabin_karp(text, pattern):
    n = LEN(text), m = LEN(pattern)
    p = 31, mod = SỐ_NGUYÊN_TỐ_LỚN
    pattern_hash = polynomial_hash(pattern, p, mod)
    window_hash = polynomial_hash(text[0:m], p, mod)
    p_pow = p^(m-1) MOD mod

    FOR i IN 0..n-m:
        IF window_hash == pattern_hash AND text[i:i+m] == pattern:
            RETURN i                     // tìm thấy, xác nhận lại tránh trùng hash giả
        IF i < n - m:
            // cập nhật cửa sổ O(1): bỏ ký tự đầu, thêm ký tự mới
            window_hash = ((window_hash - ASCII(text[i]) * p_pow) * p + ASCII(text[i+m])) MOD mod
    RETURN -1
```

### Bài 7. Hàm băm cho cặp / tuple
```
FUNCTION hash_pair(a, b):
    C = 1000000007
    RETURN (hash(a) * C) XOR hash(b)
```

### Bài 8. So sánh chất lượng phân bố (chi-square)
```
FUNCTION chi_square_test(keys, hash_func, m):
    observed = mảng m phần tử = 0
    FOR k IN keys:
        observed[hash_func(k) MOD m] += 1
    expected = LEN(keys) / m
    chi2 = SUM((observed[i] - expected)^2 / expected FOR i IN 0..m-1)
    RETURN chi2      // chi2 càng nhỏ, phân bố càng đều
```

### Bài 9. Băm phổ quát (Universal Hashing)
```
FUNCTION universal_hash_family(p, m):
    a = SỐ NGẪU NHIÊN trong [1, p-1]
    b = SỐ NGẪU NHIÊN trong [0, p-1]
    RETURN FUNCTION(k): RETURN ((a*k + b) MOD p) MOD m
// Vì a, b chọn ngẫu nhiên mỗi lần khởi tạo, kẻ tấn công không thể biết trước
// hàm băm cụ thể để cố tình tạo tập khóa gây va chạm hàng loạt (hash flooding)
```

### Bài 10. Phương pháp nhân (multiplication method)
```
FUNCTION hash_multiplication(k, m, A = 0.6180339887):
    frac = (k * A) MOD 1        // lấy phần thập phân của k*A
    RETURN FLOOR(m * frac)
// So với phương pháp chia (k mod m): không nhạy cảm với việc chọn m,
// hoạt động tốt với mọi m (không cần m là số nguyên tố)
```

### Bài 11. Hàm băm độc lập thứ tự
```
FUNCTION hash_set_order_independent(elements):
    total = 0
    FOR x IN elements:
        total = total XOR hash(x)      // hoặc total = (total + hash(x)) MOD LARGE
    RETURN total
// XOR/cộng có tính giao hoán → thứ tự phần tử không ảnh hưởng kết quả
```

### Bài 12. Tấn công hash flooding
```
// Minh họa: kẻ tấn công biết công thức hash (vd h(k) = k mod m cố định)
// → cố tình sinh nhiều khóa k1, k2, ... đều có cùng h(k) mod m
// → tất cả rơi vào 1 bucket → chaining suy biến thành danh sách liên kết O(n)

// Phòng chống: dùng Universal Hashing (Bài 9) với a, b ngẫu nhiên bí mật,
// khiến kẻ tấn công không thể tính trước được bucket của khóa mà họ chọn.
```

### Bài 13. Rolling hash 2 chiều
```
FUNCTION hash_2d_pattern(matrix, p, q):
    // Băm theo hàng trước (rolling hash 1D cho mỗi hàng),
    // rồi băm theo cột trên các hash-hàng đó (rolling hash 1D lần 2)
    row_hashes = [polynomial_hash(row, p1, mod) FOR row IN matrix]
    FOR mỗi cửa sổ p hàng liên tiếp:
        col_hash = polynomial_hash(row_hashes[cửa sổ], p2, mod)
        SO SÁNH với hash của khối p×q cần tìm
```

### Bài 14. Bloom Filter
```
CLASS BloomFilter:
    bits = mảng m bit = 0
    hash_funcs = danh sách k hàm băm độc lập

    FUNCTION add(x):
        FOR h IN hash_funcs:
            bits[h(x) MOD m] = 1

    FUNCTION might_contain(x):
        FOR h IN hash_funcs:
            IF bits[h(x) MOD m] == 0:
                RETURN false        // chắc chắn KHÔNG có
        RETURN true                  // CÓ THỂ có (có thể là dương tính giả)
// Xác suất dương tính giả ≈ (1 - e^(-kn/m))^k
```

### Bài 15. MinHash ước lượng độ tương đồng
```
FUNCTION minhash_signature(set_A, hash_funcs):
    signature = []
    FOR h IN hash_funcs:
        signature.append(MIN(h(x) FOR x IN set_A))
    RETURN signature

FUNCTION estimate_jaccard(set_A, set_B, hash_funcs):
    sig_A = minhash_signature(set_A, hash_funcs)
    sig_B = minhash_signature(set_B, hash_funcs)
    matches = COUNT(i WHERE sig_A[i] == sig_B[i])
    RETURN matches / LEN(hash_funcs)     // ước lượng |A∩B| / |A∪B|
```