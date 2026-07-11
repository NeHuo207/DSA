## PHẦN A — ARRAY LIST

### Bài 1. Cài đặt Array List cơ bản
```
CLASS ArrayList:
    arr = mảng rỗng

    FUNCTION add(x): arr.append(x)
    FUNCTION get(i): RETURN arr[i]
    FUNCTION set(i, x): arr[i] = x
    FUNCTION size(): RETURN LEN(arr)
```

### Bài 2. Thêm / xóa ở cuối
```
FUNCTION append(list, x): list.arr.append(x)
FUNCTION popBack(list):
    x = list.arr[LEN(list.arr) - 1]
    REMOVE phần tử cuối
    RETURN x
```

### Bài 3. Chèn / xóa ở vị trí bất kỳ
```
FUNCTION insert_at(list, i, x):
    DỊCH mọi phần tử từ cuối về vị trí i sang phải 1 ô
    list.arr[i] = x

FUNCTION remove_at(list, i):
    x = list.arr[i]
    DỊCH mọi phần tử sau i sang trái 1 ô
    RETURN x
```

### Bài 4. Tìm kiếm tuyến tính
```
FUNCTION indexOf(list, target):
    FOR i IN 0..LEN(list.arr)-1:
        IF list.arr[i] == target: RETURN i
    RETURN -1
```

### Bài 5. Duyệt và in phần tử
```
FUNCTION count_matching(list, condition):
    count = 0
    FOR x IN list.arr:
        PRINT x
        IF condition(x): count += 1
    RETURN count
```

### Bài 6. Tự động mở rộng dung lượng
```
FUNCTION add_with_resize(list, x):
    IF list.size == list.capacity:
        new_cap = list.capacity * 2
        new_arr = mảng kích thước new_cap
        COPY list.arr sang new_arr
        list.arr = new_arr
        list.capacity = new_cap
    list.arr[list.size] = x
    list.size += 1
```

### Bài 7. Phân tích amortized của append — chứng minh
```
// Mỗi lần resize gấp đôi tốn O(k) để copy k phần tử,
// nhưng lần resize kế tiếp chỉ xảy ra sau k lần append tiếp theo (không resize).
// Tổng chi phí copy cho n lần append: 1+2+4+...+n = O(2n) = O(n)
// → chi phí amortized mỗi append = O(n)/n = O(1)
```

### Bài 8. Xóa các phần tử thỏa điều kiện (removeIf)
```
FUNCTION remove_if(arr, condition):
    write = 0
    FOR read IN 0..LEN(arr)-1:
        IF NOT condition(arr[read]):
            arr[write] = arr[read]
            write += 1
    TRUNCATE arr đến độ dài write
    RETURN arr
```

### Bài 9. Đảo ngược tại chỗ
```
FUNCTION reverse_inplace(arr):
    left = 0, right = LEN(arr) - 1
    WHILE left < right:
        SWAP(arr[left], arr[right])
        left += 1; right -= 1
```

### Bài 10. Trộn hai danh sách đã sắp xếp
```
FUNCTION merge_sorted(a, b):
    result = [], i = 0, j = 0
    WHILE i < LEN(a) AND j < LEN(b):
        IF a[i] <= b[j]: result.append(a[i]); i += 1
        ELSE: result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    RETURN result
```

### Bài 11. Xoay mảng k vị trí (đảo ba lần)
```
FUNCTION rotate_right(arr, k):
    n = LEN(arr); k = k MOD n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    RETURN arr

FUNCTION reverse(arr, l, r):
    WHILE l < r: SWAP(arr[l], arr[r]); l+=1; r-=1
```

### Bài 12. Loại bỏ trùng lặp giữ thứ tự
```
// Cách O(n^2):
FUNCTION dedup_slow(arr):
    result = []
    FOR x IN arr:
        IF x NOT IN result: result.append(x)
    RETURN result

// Cách O(n) dùng tập băm:
FUNCTION dedup_fast(arr):
    seen = set(), result = []
    FOR x IN arr:
        IF x NOT IN seen:
            seen.add(x); result.append(x)
    RETURN result
```

### Bài 13. Trộn các khoảng (Merge Intervals)
```
FUNCTION merge_intervals(intervals):
    SORT intervals theo start tăng dần
    result = [intervals[0]]
    FOR i IN 1..LEN(intervals)-1:
        last = result[-1]
        IF intervals[i].start <= last.end:
            last.end = MAX(last.end, intervals[i].end)
        ELSE:
            result.append(intervals[i])
    RETURN result
```

### Bài 14. Mảng động 2 chiều
```
CLASS DynamicMatrix:
    rows = danh sách các ArrayList

    FUNCTION add_row():
        rows.append(ArrayList())

    FUNCTION set(i, j, val):
        rows[i].set(j, val)

    FUNCTION get(i, j):
        RETURN rows[i].get(j)
```

### Bài 15. Iterator và fail-fast
```
CLASS ArrayListIterator:
    list, idx = 0, expected_modCount = list.modCount

    FUNCTION hasNext(): RETURN idx < list.size

    FUNCTION next():
        IF list.modCount != expected_modCount:
            ERROR "ConcurrentModificationException"
        x = list.arr[idx]; idx += 1
        RETURN x

// Mọi thao tác add/remove trên list phải tăng list.modCount += 1
```

## PHẦN B — LINKED LIST

### Bài 1. Cài đặt danh sách liên kết đơn
```
CLASS Node: value, next = null

CLASS LinkedList:
    head = null, tail = null

    FUNCTION pushFront(x):
        node = Node(x); node.next = head; head = node
        IF tail == null: tail = node

    FUNCTION pushBack(x):
        node = Node(x)
        IF head == null: head = tail = node
        ELSE: tail.next = node; tail = node

    FUNCTION print_all():
        cur = head
        WHILE cur != null:
            PRINT cur.value; cur = cur.next
```

### Bài 2. Tính độ dài / duyệt
```
FUNCTION length(head):
    count = 0, cur = head
    WHILE cur != null:
        count += 1; cur = cur.next
    RETURN count
```

### Bài 3. Tìm kiếm một giá trị
```
FUNCTION find(head, target):
    cur = head, idx = 0
    WHILE cur != null:
        IF cur.value == target: RETURN idx
        cur = cur.next; idx += 1
    RETURN -1
```

### Bài 4. Chèn sau một nút cho trước
```
FUNCTION insert_after(prev_node, x):
    node = Node(x)
    node.next = prev_node.next
    prev_node.next = node
```

### Bài 5. Xóa nút theo giá trị
```
FUNCTION delete_value(head, x):
    IF head == null: RETURN head
    IF head.value == x: RETURN head.next
    cur = head
    WHILE cur.next != null:
        IF cur.next.value == x:
            cur.next = cur.next.next
            RETURN head
        cur = cur.next
    RETURN head
```

### Bài 6. Đảo ngược danh sách liên kết
```
// Cách lặp (3 con trỏ):
FUNCTION reverse_iterative(head):
    prev = null, cur = head
    WHILE cur != null:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    RETURN prev

// Cách đệ quy:
FUNCTION reverse_recursive(head):
    IF head == null OR head.next == null: RETURN head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = null
    RETURN new_head
```

### Bài 7. Tìm nút giữa (slow/fast)
```
FUNCTION find_middle(head):
    slow = head, fast = head
    WHILE fast != null AND fast.next != null:
        slow = slow.next
        fast = fast.next.next
    RETURN slow
```

### Bài 8. Phát hiện chu trình (Floyd)
```
FUNCTION has_cycle(head):
    slow = head, fast = head
    WHILE fast != null AND fast.next != null:
        slow = slow.next
        fast = fast.next.next
        IF slow == fast: RETURN true
    RETURN false
```

### Bài 9. Trộn hai danh sách liên kết đã sắp xếp
```
FUNCTION merge_sorted_lists(l1, l2):
    dummy = Node(0); tail = dummy
    WHILE l1 != null AND l2 != null:
        IF l1.value <= l2.value:
            tail.next = l1; l1 = l1.next
        ELSE:
            tail.next = l2; l2 = l2.next
        tail = tail.next
    tail.next = (l1 != null) ? l1 : l2
    RETURN dummy.next
```

### Bài 10. Xóa nút thứ k từ cuối
```
FUNCTION remove_kth_from_end(head, k):
    dummy = Node(0); dummy.next = head
    fast = dummy, slow = dummy
    FOR i IN 1..k: fast = fast.next
    WHILE fast.next != null:
        fast = fast.next; slow = slow.next
    slow.next = slow.next.next
    RETURN dummy.next
```

### Bài 11. Danh sách liên kết đôi
```
CLASS DNode: value, prev = null, next = null

CLASS DoublyLinkedList:
    head = null, tail = null

    FUNCTION pushFront(x):
        node = DNode(x)
        node.next = head
        IF head != null: head.prev = node
        head = node
        IF tail == null: tail = node

    FUNCTION pushBack(x):
        node = DNode(x)
        node.prev = tail
        IF tail != null: tail.next = node
        tail = node
        IF head == null: head = node
```

### Bài 12. Tìm điểm bắt đầu chu trình (Floyd giai đoạn 2)
```
FUNCTION find_cycle_start(head):
    slow = head, fast = head
    WHILE fast != null AND fast.next != null:
        slow = slow.next; fast = fast.next.next
        IF slow == fast: BREAK
    IF fast == null OR fast.next == null: RETURN null   // không có chu trình

    ptr1 = head, ptr2 = slow
    WHILE ptr1 != ptr2:
        ptr1 = ptr1.next; ptr2 = ptr2.next
    RETURN ptr1
```

### Bài 13. Sắp xếp danh sách liên kết (merge sort)
```
FUNCTION sort_list(head):
    IF head == null OR head.next == null: RETURN head
    mid = find_middle(head)
    right = mid.next
    mid.next = null                  // tách đôi
    left_sorted = sort_list(head)
    right_sorted = sort_list(right)
    RETURN merge_sorted_lists(left_sorted, right_sorted)
```

### Bài 14. Cộng hai số biểu diễn bằng linked list
```
FUNCTION add_two_numbers(l1, l2):
    dummy = Node(0); tail = dummy
    carry = 0
    WHILE l1 != null OR l2 != null OR carry != 0:
        v1 = (l1 != null) ? l1.value : 0
        v2 = (l2 != null) ? l2.value : 0
        total = v1 + v2 + carry
        carry = total / 10
        tail.next = Node(total MOD 10)
        tail = tail.next
        IF l1 != null: l1 = l1.next
        IF l2 != null: l2 = l2.next
    RETURN dummy.next
```

### Bài 15. LRU Cache
```
CLASS LRUCache:
    capacity, map = {}                          // key -> DNode
    dll = DoublyLinkedList()                      // head = mới nhất, tail = cũ nhất

    FUNCTION get(key):
        IF key NOT IN map: RETURN -1
        node = map[key]
        dll.move_to_front(node)
        RETURN node.value

    FUNCTION put(key, value):
        IF key IN map:
            node = map[key]; node.value = value
            dll.move_to_front(node)
        ELSE:
            IF LEN(map) == capacity:
                lru = dll.tail
                dll.remove(lru)
                DELETE map[lru.key]
            node = DNode(key, value)
            dll.push_front(node)
            map[key] = node
```