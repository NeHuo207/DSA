"""
Chứng minh:
- Mỗi lần resize gấp đôi (từ cap k lên 2k) tốn O(k) để copy k phần tử.
- Nhưng resize chỉ xảy ra khi ĐẦY, tức sau ít nhất k/2 lần append kể từ
  lần resize trước (bảng đi từ k/2 phần tử lên k phần tử).
- Tổng chi phí copy cho n lần append liên tiếp:
      1 + 2 + 4 + 8 + ... + n  <  2n  =  O(n)
- Vậy tổng chi phí n lần append = O(n) (n lần ghi + O(n) copy)
  → chi phí amortized mỗi append = O(n)/n = O(1). ∎
"""


class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.n = 0
        self.modCount = 0

    def add(self, x):
        if self.n == self.capacity:
            self._resize(self.capacity * 2)
        self.arr[self.n] = x
        self.n += 1
        self.modCount += 1

    def get(self, i):
        if not (0 <= i < self.n):
            raise IndexError("chỉ số ngoài phạm vi")
        return self.arr[i]

    def set(self, i, x):
        if not (0 <= i < self.n):
            raise IndexError("chỉ số ngoài phạm vi")
        self.arr[i] = x

    def size(self):
        return self.n

    def _resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self.n):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_cap


def demo_amortized(num_appends):
    lst = ArrayList()
    total_copies = 0
    for i in range(num_appends):
        if lst.n == lst.capacity:
            total_copies += lst.n
        lst.add(i)
    return total_copies


n = 1000
copies = demo_amortized(n)
print(f"  {n} lần append -> tổng {copies} phép copy (< 2n = {2*n}) -> amortized O(1)")
