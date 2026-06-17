import random
"""
BÀI 21 — Bài chứng minh
 
MỆNH ĐỀ: Selection Sort luôn thực hiện đúng n(n-1)/2 phép so sánh,
          bất kể thứ tự đầu vào.
 
CHỨNG MINH:
  Vòng lặp ngoài i chạy từ 0 đến n-2 (n-1 vòng).
  Ở vòng thứ i, vòng trong j chạy từ i+1 đến n-1:
    → thực hiện đúng (n - 1 - i) phép so sánh.
 
  Tổng số so sánh:
    Σ(i=0 → n-2) (n-1-i)
    = (n-1) + (n-2) + ... + 1
    = n(n-1)/2
 
  Số này không phụ thuộc vào giá trị của a[j] vì vòng trong
  luôn chạy từ đầu đến cuối đoạn chưa sắp xếp, không dừng sớm.
 
KẾT LUẬN: Selection Sort không có "best case" nhanh hơn. □
"""
 
# Kiểm chứng bằng code
def selection_sort_count_cmps(a):
    b = a[:]
    cmps = 0
    n = len(b)

    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            cmps += 1
            if b[j] < b[mi]:
                mi = j
        b[i], b[mi] = b[mi], b[i]

    return cmps
def verify_fixed_cmps(n):
    cases = [
        list(range(n)),           # đã sắp xếp
        list(range(n, 0, -1)),    # ngược
        random.sample(range(n*2), n)  # ngẫu nhiên
    ]
    names = ["sorted", "reversed", "random"]
    expected = n * (n - 1) // 2
    for name, a in zip(names, cases):
        _, c = selection_sort_count_cmps(a)
        print(f"  {name:<10}: cmps={c}, expected={expected}, ok={c==expected}")
 
print("Bài 21:")
verify_fixed_cmps(6)