## PHẦN A — NGĂN XẾP (STACK)

### Bài 1. Cài đặt ngăn xếp bằng mảng
```
CLASS Stack:
    arr = mảng rỗng, top = -1

    FUNCTION push(x):
        top += 1
        arr[top] = x

    FUNCTION pop():
        IF isEmpty(): ERROR "underflow"
        x = arr[top]
        top -= 1
        RETURN x

    FUNCTION top_val():
        IF isEmpty(): ERROR
        RETURN arr[top]

    FUNCTION isEmpty():
        RETURN top == -1
```

### Bài 2. Đảo ngược chuỗi dùng ngăn xếp
```
FUNCTION reverse_string(s):
    st = Stack()
    FOR ch IN s: st.push(ch)
    result = ""
    WHILE NOT st.isEmpty():
        result += st.pop()
    RETURN result
```

### Bài 3. Mô phỏng dãy thao tác
```
FUNCTION simulate(ops):
    st = Stack()
    FOR op IN ops:
        IF op == ("push", x): st.push(x)
        ELSE IF op == "pop":
            PRINT st.pop()
    PRINT "stack cuối:", st.arr[0..st.top]
```

### Bài 4. Phát hiện underflow / overflow
```
CLASS BoundedStack:
    arr = mảng kích thước cap, top = -1

    FUNCTION push(x):
        IF top == cap - 1: ERROR "overflow"
        top += 1; arr[top] = x

    FUNCTION pop():
        IF top == -1: ERROR "underflow"
        x = arr[top]; top -= 1
        RETURN x
```

### Bài 5. Duyệt và đếm phần tử (giữ nguyên stack)
```
FUNCTION print_and_restore(st):
    temp = Stack()
    count = 0
    WHILE NOT st.isEmpty():
        x = st.pop()
        PRINT x
        temp.push(x)
        count += 1
    WHILE NOT temp.isEmpty():
        st.push(temp.pop())     // khôi phục đúng thứ tự ban đầu
    RETURN count
```

### Bài 6. Dấu ngoặc cân bằng
```
FUNCTION is_balanced(s):
    st = Stack()
    pairs = {')':'(', ']':'[', '}':'{'}
    FOR ch IN s:
        IF ch IN "([{":
            st.push(ch)
        ELSE IF ch IN ")]}":
            IF st.isEmpty() OR st.pop() != pairs[ch]:
                RETURN false
    RETURN st.isEmpty()
```

### Bài 7. Min Stack — getMin O(1)
```
CLASS MinStack:
    st = Stack()          // stack chính
    minSt = Stack()        // stack phụ lưu min hiện tại

    FUNCTION push(x):
        st.push(x)
        IF minSt.isEmpty() OR x <= minSt.top_val():
            minSt.push(x)
        ELSE:
            minSt.push(minSt.top_val())   // lặp lại min cũ

    FUNCTION pop():
        minSt.pop()
        RETURN st.pop()

    FUNCTION getMin():
        RETURN minSt.top_val()
```

### Bài 8. Tính biểu thức hậu tố (RPN)
```
FUNCTION eval_rpn(tokens):
    st = Stack()
    FOR tok IN tokens:
        IF tok LÀ SỐ:
            st.push(tok)
        ELSE:                       // toán tử + - * /
            b = st.pop(); a = st.pop()
            st.push(apply(a, b, tok))
    RETURN st.pop()
```

### Bài 9. Chuyển trung tố sang hậu tố (shunting-yard)
```
FUNCTION infix_to_postfix(expr):
    prec = {'+':1, '-':1, '*':2, '/':2}
    output = [], opStack = Stack()
    FOR token IN tokenize(expr):
        IF token LÀ TOÁN HẠNG:
            output.append(token)
        ELSE IF token == '(':
            opStack.push(token)
        ELSE IF token == ')':
            WHILE opStack.top_val() != '(':
                output.append(opStack.pop())
            opStack.pop()          // bỏ dấu '('
        ELSE:                       // là toán tử
            WHILE NOT opStack.isEmpty() AND opStack.top_val() != '(' 
                  AND prec[opStack.top_val()] >= prec[token]:
                output.append(opStack.pop())
            opStack.push(token)
    WHILE NOT opStack.isEmpty():
        output.append(opStack.pop())
    RETURN output
```

### Bài 10. Cài đặt ngăn xếp bằng hai hàng đợi
```
CLASS StackFromQueues:
    q1 = Queue(), q2 = Queue()

    FUNCTION push(x):
        q2.enqueue(x)
        WHILE NOT q1.isEmpty():
            q2.enqueue(q1.dequeue())
        SWAP(q1, q2)             // push O(n), pop O(1)

    FUNCTION pop():
        RETURN q1.dequeue()
```

### Bài 11. Next Greater Element (ngăn xếp đơn điệu)
```
FUNCTION next_greater(a):
    n = LEN(a)
    result = mảng n phần tử = -1
    st = Stack()                // lưu CHỈ SỐ, giữ giá trị giảm dần

    FOR i IN 0..n-1:
        WHILE NOT st.isEmpty() AND a[st.top_val()] < a[i]:
            idx = st.pop()
            result[idx] = a[i]
        st.push(i)
    RETURN result
```

### Bài 12. Hình chữ nhật lớn nhất trong histogram
```
FUNCTION largest_rectangle(h):
    st = Stack()                // lưu chỉ số, chiều cao tăng dần
    max_area = 0
    FOR i IN 0..LEN(h):
        cur = (i == LEN(h)) ? 0 : h[i]
        WHILE NOT st.isEmpty() AND h[st.top_val()] >= cur:
            height = h[st.pop()]
            width = st.isEmpty() ? i : i - st.top_val() - 1
            max_area = MAX(max_area, height * width)
        st.push(i)
    RETURN max_area
```

### Bài 13. DFS dùng ngăn xếp (khử đệ quy)
```
FUNCTION dfs_iterative(adj, start):
    visited = set(), st = Stack()
    st.push(start)
    order = []
    WHILE NOT st.isEmpty():
        u = st.pop()
        IF u IN visited: CONTINUE
        visited.add(u); order.append(u)
        FOR v IN adj[u] (theo thứ tự ngược để giống thứ tự đệ quy):
            IF v NOT IN visited:
                st.push(v)
    RETURN order
```

### Bài 14. Bài toán nhịp giá cổ phiếu (Stock Span)
```
FUNCTION stock_span(prices):
    n = LEN(prices)
    span = mảng n phần tử
    st = Stack()                // lưu chỉ số, giá giảm dần

    FOR i IN 0..n-1:
        WHILE NOT st.isEmpty() AND prices[st.top_val()] <= prices[i]:
            st.pop()
        span[i] = st.isEmpty() ? (i + 1) : (i - st.top_val())
        st.push(i)
    RETURN span
```

### Bài 15. Sắp xếp một ngăn xếp
```
FUNCTION sort_stack(st):
    aux = Stack()                // stack phụ, giữ tăng dần từ đáy lên đỉnh
    WHILE NOT st.isEmpty():
        temp = st.pop()
        WHILE NOT aux.isEmpty() AND aux.top_val() > temp:
            st.push(aux.pop())
        aux.push(temp)
    WHILE NOT aux.isEmpty():
        st.push(aux.pop())        // đổ lại, lớn nhất ở đỉnh
    RETURN st
```

## PHẦN B — HÀNG ĐỢI (QUEUE)

### Bài 1. Cài đặt hàng đợi cơ bản
```
CLASS Queue:
    arr = mảng rỗng, front_idx = 0

    FUNCTION enqueue(x):
        arr.append(x)

    FUNCTION dequeue():
        IF isEmpty(): ERROR
        x = arr[front_idx]
        front_idx += 1
        RETURN x

    FUNCTION isEmpty():
        RETURN front_idx == LEN(arr)
```

### Bài 2. Hàng đợi vòng (Circular Queue)
```
CLASS CircularQueue:
    arr = mảng kích thước cap
    front = 0, rear = 0, count = 0

    FUNCTION enqueue(x):
        IF count == cap: ERROR "đầy"
        arr[rear] = x
        rear = (rear + 1) MOD cap
        count += 1

    FUNCTION dequeue():
        IF count == 0: ERROR "rỗng"
        x = arr[front]
        front = (front + 1) MOD cap
        count -= 1
        RETURN x
```

### Bài 3. Mô phỏng dãy thao tác
```
FUNCTION simulate_queue(ops):
    q = Queue()
    FOR op IN ops:
        IF op == ("enqueue", x): q.enqueue(x)
        ELSE IF op == "dequeue": PRINT q.dequeue()
```

### Bài 4. Kiểm tra rỗng / đầy
```
FUNCTION safe_dequeue(q):
    IF q.isEmpty(): ERROR "rỗng"
    RETURN q.dequeue()

FUNCTION safe_enqueue(q, x, cap):
    IF q.count == cap: ERROR "đầy"
    q.enqueue(x)
```

### Bài 5. Tìm front và rear
```
FUNCTION peek_front(q): RETURN q.arr[q.front_idx]
FUNCTION peek_rear(q):  RETURN q.arr[LEN(q.arr) - 1]
```

### Bài 6. Cài đặt hàng đợi bằng hai ngăn xếp
```
CLASS QueueFromStacks:
    in_stack = Stack(), out_stack = Stack()

    FUNCTION enqueue(x):
        in_stack.push(x)

    FUNCTION dequeue():
        IF out_stack.isEmpty():
            WHILE NOT in_stack.isEmpty():
                out_stack.push(in_stack.pop())
        RETURN out_stack.pop()
```

### Bài 7. Đảo ngược hàng đợi
```
FUNCTION reverse_queue(q):
    st = Stack()
    WHILE NOT q.isEmpty(): st.push(q.dequeue())
    WHILE NOT st.isEmpty(): q.enqueue(st.pop())
    RETURN q
```

### Bài 8. Hàng đợi hai đầu (Deque)
```
CLASS Deque:
    arr = danh sách liên kết đôi rỗng

    FUNCTION pushFront(x): arr.insert_at_head(x)
    FUNCTION pushBack(x):  arr.insert_at_tail(x)
    FUNCTION popFront():   RETURN arr.remove_head()
    FUNCTION popBack():    RETURN arr.remove_tail()
```

### Bài 9. BFS dùng hàng đợi
```
FUNCTION bfs(adj, start):
    visited = set(), q = Queue()
    q.enqueue(start); visited.add(start)
    order = []
    WHILE NOT q.isEmpty():
        u = q.dequeue()
        order.append(u)
        FOR v IN adj[u]:
            IF v NOT IN visited:
                visited.add(v)
                q.enqueue(v)
    RETURN order
```

### Bài 10. Hàng đợi ưu tiên cơ bản
```
CLASS SimplePriorityQueue:
    arr = mảng rỗng của (priority, value)

    FUNCTION insert(p, v):
        arr.append((p, v))         // O(1) chèn, không giữ thứ tự

    FUNCTION extract_max():
        best_idx = argmax theo p trong arr    // O(n) mỗi lần lấy
        RETURN arr.pop(best_idx)
// So sánh: cài bằng heap → insert O(log n), extract O(log n)
```

### Bài 11. Giá trị lớn nhất trong cửa sổ trượt (deque đơn điệu)
```
FUNCTION max_sliding_window(a, k):
    dq = Deque()                 // lưu CHỈ SỐ, giá trị giảm dần từ đầu tới cuối
    result = []
    FOR i IN 0..LEN(a)-1:
        WHILE NOT dq.isEmpty() AND a[dq.back()] < a[i]:
            dq.popBack()
        dq.pushBack(i)
        IF dq.front() <= i - k:
            dq.popFront()          // loại chỉ số ngoài cửa sổ
        IF i >= k - 1:
            result.append(a[dq.front()])
    RETURN result
```

### Bài 12. Bài toán Josephus
```
FUNCTION josephus(n, k):
    q = Queue()
    FOR i IN 1..n: q.enqueue(i)
    WHILE LEN(q) > 1:
        FOR i IN 1..k-1:
            q.enqueue(q.dequeue())    // đẩy k-1 người ra sau
        q.dequeue()                    // loại người thứ k
    RETURN q.dequeue()                 // người sống sót
```

### Bài 13. Hàng đợi amortized O(1) từ hai ngăn xếp — chứng minh
```
// Chứng minh bằng phương pháp kế toán:
// Gán "phí" 2 đồng cho mỗi enqueue: 1 đồng trả cho push vào in_stack,
// 1 đồng "gửi tiết kiệm" để trả cho lần pop từ in_stack sang out_stack sau này.
// Mỗi phần tử chỉ được chuyển từ in_stack sang out_stack ĐÚNG 1 LẦN trong toàn bộ vòng đời
// → tổng chi phí chuyển là O(n) cho n phần tử → trung bình mỗi enqueue/dequeue là O(1).
```

### Bài 14. Trung bình trượt / đếm hit trong cửa sổ thời gian
```
CLASS SlidingWindowCounter:
    q = Queue()                  // lưu các mốc thời gian sự kiện

    FUNCTION add_event(t):
        q.enqueue(t)

    FUNCTION count_in_last(T, now):
        WHILE NOT q.isEmpty() AND q.front() <= now - T:
            q.dequeue()            // bỏ sự kiện quá hạn
        RETURN LEN(q)
```

### Bài 15. Lập lịch xoay vòng (Round-Robin)
```
FUNCTION round_robin(processes, quantum):
    // processes: danh sách (id, burst_time)
    q = Queue()
    FOR p IN processes: q.enqueue(p)
    time = 0
    completion = {}

    WHILE NOT q.isEmpty():
        (id, remaining) = q.dequeue()
        run = MIN(quantum, remaining)
        time += run
        remaining -= run
        IF remaining == 0:
            completion[id] = time
        ELSE:
            q.enqueue((id, remaining))
    RETURN completion
```
