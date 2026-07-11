"""
BÀI 22 — Phân tích đánh đổi
 
Để làm Selection Sort vừa ổn định vừa in-place:
  → Thay vì swap(a[i], a[min_idx]), ta dịch chuyển:
    1. Lưu key = a[min_idx]
    2. Dịch a[i..min_idx-1] sang phải 1 ô (như Insertion Sort!)
    3. Đặt key vào a[i]
 
Đánh đổi:
  - Swap:  O(1) mỗi vòng → tổng O(n) swap, nhưng KHÔNG ổn định
  - Shift: O(n) mỗi vòng → tổng O(n²) shift, nhưng ổn định
 
Vì phải shift O(n) mỗi vòng, Selection Sort ổn định in-place
về cơ bản hội tụ về Insertion Sort về hiệu suất thực tế.
"""
def stable_selection_sort_inplace(a):
    n = len(a)
    shifts = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
            shifts += 1
        a[i] = key
    return a, shifts
 
arr, sh = stable_selection_sort_inplace([3, 1, 2, 1])
print(f"Bài 22: {arr}, shifts={sh}")