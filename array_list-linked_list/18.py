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

    def insert_at(self, i, x):
        if not (0 <= i <= self.n):
            raise IndexError("chỉ số ngoài phạm vi")
        if self.n == self.capacity:
            self._resize(self.capacity * 2)
        for j in range(self.n, i, -1):
            self.arr[j] = self.arr[j - 1]
        self.arr[i] = x
        self.n += 1
        self.modCount += 1

    def remove_at(self, i):
        if not (0 <= i < self.n):
            raise IndexError("chỉ số ngoài phạm vi")
        x = self.arr[i]
        for j in range(i, self.n - 1):
            self.arr[j] = self.arr[j + 1]
        self.arr[self.n - 1] = None
        self.n -= 1
        self.modCount += 1
        return x

    def to_list(self):
        return [self.arr[i] for i in range(self.n)]


lst2 = ArrayList()
for x in [1, 2, 4]:
    lst2.add(x)
lst2.insert_at(2, 3)
print(f"  [1,2,4] chèn 3 tại idx 2 -> {lst2.to_list()}")
lst2.remove_at(0)
print(f"  xóa idx 0 -> {lst2.to_list()}")
